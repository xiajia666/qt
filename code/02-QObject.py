from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("$的学习")
        self.resize(500, 500)
        label = QLabel(self)
        label.setText("cool")
        label.move(500, 100)
        label.setObjectName("notice")
        with open("../file/QObject.qss", 'r') as f:
            self.setStyleSheet(f.read())
        label2 = QLabel(self)
        label2.setText("xxxx")
        label2.move(100, 100)
        label2.setObjectName("notice")
        label2.setProperty("notice_level", "normal")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
