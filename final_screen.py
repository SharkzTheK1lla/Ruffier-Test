from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, 
    QPushButton, QVBoxLayout, QWidget,
    QLabel, QLineEdit, QMessageBox)

from instr import *
from second_screen import *

class FinalWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()# mengatur seperti apa tampilan jendela
        self.initUI() # membuat dan mengkonfigurasi elemen grafis
        self.connects() # membangun hubungan antar elemen
        self.show() # start

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    # Setup Widget and Layout
    def initUI(self):
        ''' creates graphic elements '''
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)


        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)        
        self.setLayout(self.layout_line)
        
    def connects(self):
        pass