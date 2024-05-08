class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def transfer(self, recipient, amount):
        
        if not isinstance(recipient, User):
            print("Invalid recipient")
            return
        
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
        else:
            print("Insufficient funds")


    def get_transaction_history(self):
        return self.transaction_history


class ATMInterface:
    def __init__(self):
        self.users = {}  # Dictionary to store user_id -> User mapping

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None

    def display_menu(self):
        print("1. View Transactions History")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Transfer Money")
        print("5. Quit")

    def start(self):
        while True:
            print("Welcome to the ATM")
            user_id = input("Enter User ID: ")
            pin = input("Enter PIN: ")

            user = self.authenticate_user(user_id, pin)
            if user:
                print("Authentication successful")
                self.handle_transactions(user)
            else:
                print("Invalid User ID or PIN")

    def handle_transactions(self, user):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                transactions = user.get_transaction_history()
                print("Transaction History:")
                for transaction in transactions:
                    print(transaction)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                user.withdraw(amount)
            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                user.deposit(amount)
            elif choice == '4':
                recipient_id = input("Enter recipient's User ID: ")
                amount = float(input("Enter amount to transfer: "))
                if recipient_id in self.users and recipient_id != user.user_id:
                    recipient = self.users[recipient_id]
                    # Perform transfer
                    user.transfer(recipient, amount)
                    print("Transfer completed successfully")
                else:
                    print("Invalid recipient selected")
            elif choice == '5':
                print("Thank you for using the ATM")
                #exit(0)
                break
            else:
                print("Invalid choice")


# Usage example
def main():
    # Create ATM interface instance
    atm = ATMInterface()

    # Add some users
    user1 = User("123", "456")
    user2 = User("789", "012")
    user3 = User("011","222")
    user4 = User("001","000")
    atm.users[user1.user_id] = user1
    atm.users[user2.user_id] = user2
    atm.users[user3.user_id] = user3
    atm.users[user4.user_id] = user4

    # Start ATM interface
    atm.start()


if __name__ == "__main__":
    main()
