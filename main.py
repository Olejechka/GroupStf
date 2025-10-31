import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Mashinkov(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("бандит")

        screen = QApplication.primaryScreen().size()
        window_width = int(screen.width() * 0.8)
        window_height = int(screen.height() * 0.6)

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