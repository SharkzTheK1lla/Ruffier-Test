from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QPushButton, QLabel, QVBoxLayout, 
    QMessageBox, QRadioButton, QHBoxLayout)

from random import randint

app = QApplication([])

main_window = QWidget()
main_window.setWindowTitle("Quiz App!")
main_window.resize(700, 200)

lbl_question = QLabel("Kapan Indonesia Merdeka?")

rbtn_answer1 = QRadioButton("1945")
rbtn_answer2 = QRadioButton("1949")
rbtn_answer3 = QRadioButton("1944")
rbtn_answer4 = QRadioButton("1947")

layout_row1 = QHBoxLayout()
layout_row1.addWidget(rbtn_answer1, alignment = Qt.AlignmentFlag.AlignCenter)
layout_row1.addWidget(rbtn_answer2, alignment = Qt.AlignmentFlag.AlignCenter)

main_window.setLayout(layout_row1)
main_window.show()
app.exec_()