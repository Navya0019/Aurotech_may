import tkinter as tk
from time import sleep
from threading import Thread

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer Application")
        
        # Calculate the screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Set the window size and position it in the middle
        window_width = 400
        window_height = 300
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        
        self.root.configure(bg="#f0f0f0")
        
        self.is_running = False
        self.is_countdown = False
        self.time_left = 0
        self.elapsed_time = 0
        
        # Create widgets
        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 60), fg="black", bg="#f0f0f0")
        self.label.grid(row=0, column=0, columnspan=4, pady=20)

        self.start_stopwatch_button = tk.Button(root, text="Start Stopwatch", command=self.start_stopwatch, bg="#d9d9d9", fg="black")
        self.start_stopwatch_button.grid(row=1, column=0, padx=10, pady=10)

        self.start_countdown_button = tk.Button(root, text="Start Countdown", command=self.start_countdown, bg="#d9d9d9", fg="black")
        self.start_countdown_button.grid(row=1, column=1, padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop, bg="#d9d9d9", fg="black")
        self.stop_button.grid(row=1, column=2, padx=10, pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset, bg="#d9d9d9", fg="black")
        self.reset_button.grid(row=1, column=3, padx=10, pady=10)
        
        self.entry_label = tk.Label(root, text="Enter countdown time (seconds):", font=("Helvetica", 12), bg="#f0f0f0")
        self.entry_label.grid(row=2, column=0, columnspan=4, padx=10, pady=5)
        
        self.countdown_entry = tk.Entry(root, width=10, font=("Helvetica", 12))
        self.countdown_entry.grid(row=3, column=0, columnspan=4, padx=10, pady=5)
        
        self.set_button = tk.Button(root, text="Set Countdown", command=self.set_countdown, bg="#d9d9d9", fg="black")
        self.set_button.grid(row=4, column=0, columnspan=4, padx=10, pady=5)

    def update_label(self, time_str):
        self.label.config(text=time_str)
        
    def start_stopwatch(self):
        self.is_running = True
        self.is_countdown = False
        self.run_stopwatch()
        
    def start_countdown(self):
        self.set_countdown()  # Set the countdown time
        if self.is_countdown:
            self.is_running = True
            self.run_countdown()
        
    def stop(self):
        self.is_running = False

    def reset(self):
        self.is_running = False
        self.is_countdown = False
        self.time_left = 0
        self.elapsed_time = 0
        self.update_label("00:00:00")
        
    def set_countdown(self):
        try:
            self.time_left = int(self.countdown_entry.get())
            if self.time_left < 0:
                raise ValueError
            self.is_countdown = True
            self.update_label(self.format_time(self.time_left))
        except ValueError:
            self.update_label("Invalid Input")

    def run_countdown(self):
        def countdown():
            while self.time_left >= 0 and self.is_running:
                self.update_label(self.format_time(self.time_left))
                sleep(1)
                self.time_left -= 1
            if self.time_left == -1:
                self.update_label("00:00:00")
                self.is_running = False
                
        Thread(target=countdown).start()
        
    def run_stopwatch(self):
        def stopwatch():
            while self.is_running:
                self.update_label(self.format_time(self.elapsed_time))
                sleep(1)
                self.elapsed_time += 1
                
        Thread(target=stopwatch).start()

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
