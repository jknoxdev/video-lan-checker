import ecdsa
import os
import qrcode
from PIL import Image
#from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
#from PyQt5.QtGui import QPixmap, QImage, QPalette

#from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
#from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage, QPalette, QColor  # Import QColor


class ECDSApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.load_images()
        self.create_labels()

    def load_images(self):
        self.private_key_qr_image = Image.open("keys/private_key_qr_code.png")
        self.public_key_qr_image = Image.open("keys/public_key_qr_code.png")
        self.elliptical_curve_qr_image = Image.open("keys/elliptical_curve_qr_code.png")

    def create_labels(self):
        layout = QVBoxLayout()

        private_key_qr_label = QLabel("Private Key QR Code")
        private_key_qr_pixmap = QPixmap.fromImage(self.convert_pil_to_qimage(self.private_key_qr_image))
        private_key_qr_label.setPixmap(private_key_qr_pixmap)
        private_key_qr_label.setStyleSheet("color: white; font-size: 14px; background-color: #222222;")
        layout.addWidget(private_key_qr_label)

        public_key_qr_label = QLabel("Public Key QR Code")
        public_key_qr_pixmap = QPixmap.fromImage(self.convert_pil_to_qimage(self.public_key_qr_image))
        public_key_qr_label.setPixmap(public_key_qr_pixmap)
        public_key_qr_label.setStyleSheet("color: white; font-size: 14px; background-color: #222222;")
        layout.addWidget(public_key_qr_label)

        elliptical_curve_qr_label = QLabel("Elliptical Curve QR Code")
        elliptical_curve_qr_pixmap = QPixmap.fromImage(self.convert_pil_to_qimage(self.elliptical_curve_qr_image))
        elliptical_curve_qr_label.setPixmap(elliptical_curve_qr_pixmap)
        elliptical_curve_qr_label.setStyleSheet("color: white; font-size: 14px; background-color: #222222;")
        layout.addWidget(elliptical_curve_qr_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def convert_pil_to_qimage(self, pil_image):
        image_data = pil_image.convert("RGBA").tobytes("raw", "RGBA")
        qimage = QImage(image_data, pil_image.width, pil_image.height, QImage.Format_RGBA8888)
        return qimage

def main():
    app = QApplication([])
    window = ECDSApp()
    window.setWindowTitle("Elliptical Curve Digital Signature Algorithm")
    window.setGeometry(100, 100, 800, 600)

      # Set dark mode palette
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(30, 30, 30))
    palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
    app.setPalette(palette)

    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
