import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox,QSlider
from PyQt5.QtCore import Qt, QTimer, QRect, QSize, QUrl, QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QPainter, QPixmap, QFont,QIcon,QMovie
from PyQt5 import QtWidgets

class Mashinkov(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Бандит.exe")

        screen = QApplication.primaryScreen().size()
        window_width = int(screen.width() * 0.7)
        window_height = int(screen.height() * 0.7)

        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile("mat/Blue_Moon.mp3")))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.music_player = QMediaPlayer()
        self.music_player.setPlaylist(self.playlist)
        self.music_player.play()

        def play_music(self):
            self.music_player.play()

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, window_width, window_height)
        self.background_label.setScaledContents(True)
        self.background_image = QPixmap("mat/new2.png")
        self.background_label.setPixmap(self.background_image)

        self.play_button = QPushButton(self)
        self.play_button.setGeometry(-50, 0, 200, 100)
        self.play_button.setStyleSheet("border: none;")
        self.play_button.setIcon(QIcon("mat/info.png"))
        self.play_button.setIconSize(QSize(50, 200))
        self.play_button.clicked.connect(self.show_info)

        self.kartinka_label = QLabel(self)
        self.kartinka_label.setGeometry(300, 0, 700, 790)
        self.kartinka_label.setScaledContents(True)
        self.kartinka_image = QPixmap("mat/bb.png")
        self.kartinka_label.setPixmap(self.kartinka_image)

        self.setFixedSize(window_width, window_height)

        self.move(
            (screen.width() - window_width) // 2,
            (screen.height() - window_height) // 2
        )

    def show_info(self):
        new_pixmap = QPixmap("mat/black.png")
        if not new_pixmap.isNull():
            width = 1500
            height = 1100
            scaled_pixmap = new_pixmap.scaled(
                width, height,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            self.kartinka_label.setPixmap(scaled_pixmap)
            self.kartinka_label.setScaledContents(False)
            self.kartinka_label.show()
        else:
            pass

        if not hasattr(self, 'end_button'):
            self.end_button = QPushButton(self)
            self.end_button.setGeometry(850, 0, 200, 100)
            self.end_button.setStyleSheet("border: none;")
            self.end_button.setIcon(QIcon("mat/end.png"))
            self.end_button.setIconSize(QSize(25, 75))
            self.end_button.clicked.connect(self.end)

        self.end_button.show()

    def end(self):
        self.kartinka_label.clear()
        self.end_button.hide()
        self.kartinka_label.setPixmap(QPixmap("mat/bb.png"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mashinkov()
    window.show()
    sys.exit(app.exec())