from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QMessageBox)

app = QApplication([])

main_window = QMainWindow()
main_window.setWindowTitle("WebE")
main_window.resize(700, 500)

lbl_title = QLabel("Press the button to generate number!")
lbl_result = QLabel("???")
btn_generate = QPushButton("Generate!")

layout_main = QVBoxLayout()
layout_main.addWidget(lbl_title, alignment=Qt.AlignCenter)
layout_main.addWidget(lbl_result, alignment=Qt.AlignCenter)
layout_main.addWidget(btn_generate, alignment=Qt.AlignCenter)

def random_number():
    number = randint(65, 67)
    lbl_result.setText(str(number))
    
btn_generate.clicked.connect(random_number)


central_widget = QWidget()
central_widget.setLayout(layout_main)
main_window.setCentralWidget(central_widget)

main_window.show()
app.exec_()