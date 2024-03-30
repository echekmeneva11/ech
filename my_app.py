from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from second_win import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next = QPushButton('txt_next', self)
        self.hello_text = QLabel('txt_hello')
        self.hello2_text = QLabel('hello')
        self.instruction = QLabel('txt_instruction')
        self.instruction2 = QLabel('txt')
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.hello2_text, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction2, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        win_x, win_y = 200, 100
        win_width, win_height = 1000, 600
        self.setWindowTitle('txt_title')
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
app = QApplication([])
mw = TestWin()
app.exec_()