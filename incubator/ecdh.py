import ecdsa
import os
import qrcode
import tkinter as tk
from PIL import Image
import matplotlib.pyplot as plt

class ECDSApp:
    def __init__(self, window):
        self.window = window

        self.load_images()
        self.create_labels()

    def load_images(self):
        self.private_key_qr_image = Image.open("keys/private_key_qr_code.png")
        self.public_key_qr_image = Image.open("keys/public_key_qr_code.png")
        self.elliptical_curve_qr_image = Image.open("keys/elliptical_curve_qr_code.png")

    def create_labels(self):
        private_key_qr_label = tk.Label(self.window, text="Private Key QR Code", bg="black", fg="white")
        private_key_qr_label.place(x=0, y=200)

        public_key_qr_label = tk.Label(self.window, text="Public Key QR Code", bg="black", fg="white")
        public_key_qr_label.place(x=0, y=400)

        elliptical_curve_qr_label = tk.Label(self.window, text="Elliptical Curve QR Code", bg="black", fg="white")
        elliptical_curve_qr_label.place(x=0, y=600)

def main():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window = tk.Tk()
    window.title("Elliptical Curve Digital Signature Algorithm")
    window.geometry(str(screen_width-100) + "x" + str(screen_height-100))
    window.configure(background='black')

    app = ECDSApp(window)

    plt.figure(figsize=(3, 3))
    plt.imshow(app.private_key_qr_image)
    plt.axis('off')
    plt.show()

    plt.figure(figsize=(3, 3))
    plt.imshow(app.public_key_qr_image)
    plt.axis('off')
    plt.show()

    plt.figure(figsize=(3, 3))
    plt.imshow(app.elliptical_curve_qr_image)
    plt.axis('off')
    plt.show()

    window.mainloop()

if __name__ == "__main__":
    main()
