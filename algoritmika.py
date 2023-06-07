import time
from PyQt5.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QWidget, QLabel, QPushButton, QVBoxLayout, QRadioButton, QMessageBox, QButtonGroup
from PyQt5.QtCore import Qt, QTimer
from random import randint

def clearLayout(layout):
    
    if layout is not None:
        while layout.count():
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())

def window_1():
    welcome = QLabel()
    welcome.setText('Добро пожаловать!')
    rules = QLabel()
    rules.setText('tut tipo mnogo pravil i obyasneniy')
    continue_button = QPushButton()
    continue_button.setText('Продолжить')

    vline1 = QVBoxLayout()
    vline1.addWidget(welcome, alignment=Qt.AlignLeft)
    vline1.addWidget(rules, alignment=Qt.AlignLeft)
    vline1.addWidget(continue_button, alignment=Qt.AlignBottom)

    continue_button.clicked.connect(window_2)
    all_lines.addLayout(vline1)
    window.setLayout(all_lines)
    window.show()

def window_2():

    def timer(t):
        clock.setText(str(t))
        if t <= 0:
            return
        QTimer.singleShot(1000, lambda: timer(t-1))


    clearLayout(all_lines)

    clock = QLabel()
    clock.setText('00')

    name = QLabel()
    name.setText('Введите ваше ФИО!')
    age = QLabel()
    age.setText('Полных лет:')
    WhatToDo1 = QLabel()
    WhatToDo1.setText('Лягьте на спину ________________-')
    WhatToDo2 = QLabel()
    WhatToDo2.setText('Выполните 30 приседаний')
    WhatToDo3 = QLabel()
    WhatToDo3.setText('блаблаблабла')

    name_input = QLineEdit()
    age_input = QLineEdit()
    puls1 = QLineEdit()
    puls2 = QLineEdit()
    puls3 = QLineEdit()

    start_button1 = QPushButton()
    start_button2 = QPushButton()
    start_button3 = QPushButton()
    final_button = QPushButton()
    start_button1.setText('Начать первый тест')
    start_button2.setText('Начать делать приседания')
    start_button3.setText('Начать финальный тест')
    final_button.setText('Продолжить')

    vline1 = QVBoxLayout()
    vline2 = QVBoxLayout()

    vline1.addWidget(name, alignment=Qt.AlignLeft)
    vline1.addWidget(name_input, alignment=Qt.AlignLeft)
    vline1.addWidget(age, alignment=Qt.AlignLeft)
    vline1.addWidget(age_input, alignment=Qt.AlignLeft)
    vline1.addWidget(WhatToDo1, alignment=Qt.AlignLeft)
    vline1.addWidget(start_button1, alignment=Qt.AlignLeft)
    vline1.addWidget(puls1, alignment=Qt.AlignLeft)
    vline1.addWidget(WhatToDo2, alignment=Qt.AlignLeft)
    vline1.addWidget(start_button2, alignment=Qt.AlignLeft)
    vline1.addWidget(WhatToDo3, alignment=Qt.AlignLeft)
    vline1.addWidget(start_button3, alignment=Qt.AlignLeft)
    vline1.addWidget(puls2, alignment=Qt.AlignLeft)
    vline1.addWidget(puls3, alignment=Qt.AlignLeft)
    vline1.addWidget(final_button, alignment=Qt.AlignRight)

    vline2.addWidget(clock, alignment=Qt.AlignRight)

    start_button1.clicked.connect(lambda: timer(15))
    start_button2.clicked.connect(lambda: timer(45))
    start_button3.clicked.connect(lambda: timer(60))

    all_lines.addLayout(vline1)
    all_lines.addLayout(vline2)

    window.setLayout(all_lines)
    window.show()



app = QApplication([])

window = QWidget()
window.setWindowTitle('Правила теста')
window.setFixedHeight(500)
window.setFixedWidth(500)
all_lines = QHBoxLayout()


window_1()
app.exec_()
