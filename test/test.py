from PyQt5.Qt import *
import sys


class A:
    def __init__(self):
        self.a = 1
        print("aaa")


class B(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.b = 2
        # QWidget().setWindowTitle("qaq")
        self.setWindowTitle("qaq")
        self.setup()
        print("sss")
    def setup(self):
        print("qa")

app = QApplication(sys.argv)
C = B()
C.show()
sys.exit(app.exec_())
