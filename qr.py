import qrcode
import qrcode.constants

def createqr(data):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )

    qr.add_data(data)
    qr.make(fit = True)

    img = qr.make_image(fill='black',back_color = 'white')
    img.save("myqr.png")


def main():
    data = input("Enter the data (URL, text, etc.) to encode: ")
    createqr(data)

if __name__ == "__main__" :
    main()
    