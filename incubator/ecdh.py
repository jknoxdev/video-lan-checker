import ecdsa
import os
import qrcode
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage  # Import QImage

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
        layout.addWidget(private_key_qr_label)

        public_key_qr_label = QLabel("Public Key QR Code")
        public_key_qr_pixmap = QPixmap.fromImage(self.convert_pil_to_qimage(self.public_key_qr_image))
        public_key_qr_label.setPixmap(public_key_qr_pixmap)
        layout.addWidget(public_key_qr_label)

        elliptical_curve_qr_label = QLabel("Elliptical Curve QR Code")
        elliptical_curve_qr_pixmap = QPixmap.fromImage(self.convert_pil_to_qimage(self.elliptical_curve_qr_image))
        elliptical_curve_qr_label.setPixmap(elliptical_curve_qr_pixmap)
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
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
