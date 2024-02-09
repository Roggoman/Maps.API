import sys


from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
import requests

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi('main_window.ui', self)
        self.press_delta = 0.00001

        self.map_zoom = 6
        self.map_ll = [37.977751, 55.757718]
        self.map_l = 'map'
        self.map_key = '40d1649f-0493-4b70-98ba-98533de7710b'

        self.refresh_map()

    def refresh_map(self):
        map_params = {
            "ll": ','.join(map(str, self.map_ll)),
            "l": self.map_l,
            'z': self.map_zoom
        }
        session = requests.Session()
        response = session.get('https://static-maps.yandex.ru/1.x/',
                                params=map_params)
        with open('tmp.png', mode='wb') as tmp:
            tmp.write(response.content)

        pixmap = QPixmap()
        pixmap.load('tmp.png')
        self.g_map.setPixmap(pixmap)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())