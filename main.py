import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


class Mashinkov(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Бандит.exe")

        screen = QApplication.primaryScreen().size()
        window_width = int(screen.width() * 0.8)
        window_height = int(screen.height() * 0.6)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, window_width, window_height)
        self.background_label.setScaledContents(True)
        self.background_image = QPixmap("mat/maxresdefault.jpg")
        self.background_label.setPixmap(self.background_image)

        self.setFixedSize(window_width, window_height)

        self.move(
            (screen.width() - window_width) // 2,
            (screen.height() - window_height) // 2
        )

        self.setStyleSheet("background-color: #2c3e50;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mashinkov()
    window.show()
    sys.exit(app.exec())