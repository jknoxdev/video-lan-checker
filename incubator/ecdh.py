import ecdsa
import os
import qrcode
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage, QPalette, QColor

class ECDSApp(QMainWindow):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        self.setGeometry(100, 100, screen_width, screen_height)
        self.setWindowTitle("Elliptical Curve Digital Signature Algorithm")

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
        self.setPalette(palette)

        self.load_images()
        self.create_labels()

    def load_images(self):
        self.private_key_qr_image = Image.open("keys/private_key_qr_code.png")
        self.public_key_qr_image = Image.open("keys/public_key_qr_code.png")
        self.elliptical_curve_qr_image = Image.open("keys/elliptical_curve_qr_code.png")

    def create_labels(self):
        layout = QGridLayout()

        # Add titles for each column
        column_titles = ["Coords", "Values", "QR Code"]
        for col, title in enumerate(column_titles):
            title_label = QLabel(title)
            title_label.setStyleSheet("color: white; font-size: 14px; background-color: #222222;")
            layout.addWidget(title_label, 0, col)  # Row 0, Column col

        # Calculate QR code size based on available space
        qr_size = self.calculate_qr_size(layout)

        # Set thumbnail size for QR codes (width, height)
        thumbnail_size = (qr_size, qr_size)

        private_key_qr_label = QLabel("Private Key QR Code")
        private_key_qr_label.setPixmap(self.convert_pil_to_pixmap(self.private_key_qr_image, thumbnail_size))
        private_key_qr_label.setStyleSheet("color: white; font-size: 14px; background-color: #222222;")
        layout.addWidget(private_key_qr_label, 1, 2)  # Row 1, Column 2

        public_key_qr_label = QLabel("Public Key QR Code")
        public_key_qr_label.setPixmap(self.convert_pil_to_pixmap(self.public_key_qr_image, thumbnail_size))
        public_key_qr_label.setStyleSheet("color: white; font-size: 14px; background-color: #222222;")
        layout.addWidget(public_key_qr_label, 2, 2)  # Row 2, Column 2

        elliptical_curve_qr_label = QLabel("Elliptical Curve QR Code")
        elliptical_curve_qr_label.setPixmap(self.convert_pil_to_pixmap(self.elliptical_curve_qr_image, thumbnail_size))
        elliptical_curve_qr_label.setStyleSheet("color: white; font-size: 14px; background-color: #222222;")
        layout.addWidget(elliptical_curve_qr_label, 3, 2)  # Row 3, Column 2

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def calculate_qr_size(self, layout):
        qr_column = 2  # Column index for QR codes
        qr_width = layout.columnMinimumWidth(qr_column)
        qr_height = layout.rowMinimumHeight(3)  # Row index for last row containing QR codes

        return min(qr_width, qr_height) - 10  # Use the smaller dimension with a small buffer

    def convert_pil_to_pixmap(self, pil_image, size):
        pil_image.thumbnail((size, size))  # Resize without antialiasing
        qimage = self.convert_pil_to_qimage(pil_image)
        pixmap = QPixmap.fromImage(qimage)
        return pixmap

    def convert_pil_to_qimage(self, pil_image):
        image_data = pil_image.convert("RGBA").tobytes("raw", "RGBA")
        qimage = QImage(image_data, pil_image.width, pil_image.height, QImage.Format_RGBA8888)
        return qimage

def calculate_screen_size():
    app = QApplication([])
    screen = app.primaryScreen()
    screen_geometry = screen.geometry()
    screen_width = screen_geometry.width() - 100
    screen_height = screen_geometry.height() - 100
    return screen_width, screen_height

def main():
    screen_width, screen_height = calculate_screen_size()
    app = QApplication([])

    window = ECDSApp(screen_width, screen_height)
    window.show()

    app.exec_()

if __name__ == "__main__":
    main()
