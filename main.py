import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox,QSlider
from PyQt5.QtCore import Qt, QTimer, QRect, QSize,QUrl
from PyQt5.QtGui import QPainter, QPixmap, QFont,QIcon,QMovie
from PyQt5 import QtWidgets

class Mashinkov(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Бандит.exe")

        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile("mat/Blue_Moon.mp3")))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        #
        self.music_player = QMediaPlayer()
        self.music_player.setPlaylist(self.playlist)
        self.music_player.play()

        def play_music(self):
            self.music_player.play()

        screen = QApplication.primaryScreen().size()
        window_width = int(screen.width() * 0.7)
        window_height = int(screen.height() * 0.7)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, window_width, window_height)
        self.background_label.setScaledContents(True)
        self.background_image = QPixmap("mat/new2.png")
        self.background_label.setPixmap(self.background_image)

        self.background_label = QLabel(self)
        self.background_label.setGeometry(300, 0, 700, 790)
        self.background_label.setScaledContents(True)
        self.background_image = QPixmap("mat/bb.png")
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