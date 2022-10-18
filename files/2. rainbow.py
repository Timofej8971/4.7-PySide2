#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Решите задачу: напишите программу, состоящую из семи кнопок, цвета которых
соответствуют цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен
вставляться код цвета, а в метку – название цвета.
Коды цветов в шестнадцатеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый,
#ffff00 – желтый, #00ff00 – зеленый, #007dff – голубой, #0000ff – синий, #7d00ff –
фиолетовый.
"""

from PySide2.QtWidgets import (QApplication, QWidget,
                               QLabel, QPushButton, QLineEdit, QVBoxLayout)
from PySide2.QtCore import Qt
import sys


def main():
    app = QApplication(sys.argv)
    window = Rainbow()
    window.show()
    sys.exit(app.exec_())


class Rainbow(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('None', self)
        self.line_edit = QLineEdit('None', self)
        self.red_button = QPushButton(self)
        self.orange_button = QPushButton(self)
        self.yellow_button = QPushButton(self)
        self.green_button = QPushButton(self)
        self.blue_button = QPushButton(self)
        self.dark_blue_button = QPushButton(self)
        self.violet_button = QPushButton(self)

        self.initial_ui()

    def initial_ui(self):
        self.setGeometry(100, 100, 100, 400)
        self.setWindowTitle('Радуга')

        box_layout = QVBoxLayout()
        box_layout.addWidget(self.label)
        box_layout.addWidget(self.line_edit)
        box_layout.addWidget(self.red_button)
        box_layout.addWidget(self.orange_button)
        box_layout.addWidget(self.yellow_button)
        box_layout.addWidget(self.green_button)
        box_layout.addWidget(self.blue_button)
        box_layout.addWidget(self.dark_blue_button)
        box_layout.addWidget(self.violet_button)
        self.setLayout(box_layout)

        self.label.setAlignment(Qt.AlignCenter)
        self.line_edit.setAlignment(Qt.AlignCenter)

        self.red_button.setStyleSheet('background-color: #ff0000;')
        self.orange_button.setStyleSheet('background-color: #ff7d00;')
        self.yellow_button.setStyleSheet('background-color: #ffff00;')
        self.green_button.setStyleSheet('background-color: #00ff00;')
        self.blue_button.setStyleSheet('background-color: #007dff;')
        self.dark_blue_button.setStyleSheet('background-color: #0000ff;')
        self.violet_button.setStyleSheet('background-color: #7d00ff;')

        self.red_button.clicked.connect(self.change_label_red)
        self.orange_button.clicked.connect(self.change_label_orange)
        self.yellow_button.clicked.connect(self.change_label_yellow)
        self.green_button.clicked.connect(self.change_label_green)
        self.blue_button.clicked.connect(self.change_label_blue)
        self.dark_blue_button.clicked.connect(self.change_label_dark_blue)
        self.violet_button.clicked.connect(self.change_label_violet)

    def change_label_red(self):
        self.label.setText('Красный')
        self.line_edit.setText("#ff0000")

    def change_label_orange(self):
        self.label.setText('Оранжевый')
        self.line_edit.setText("#ff7d00")

    def change_label_yellow(self):
        self.label.setText('Жёлтый')
        self.line_edit.setText("#ffff00")

    def change_label_green(self):
        self.label.setText('Зелёный')
        self.line_edit.setText("#00ff00")

    def change_label_blue(self):
        self.label.setText('Голубой')
        self.line_edit.setText("#007dff")

    def change_label_dark_blue(self):
        self.label.setText('Синий')
        self.line_edit.setText("#0000ff")

    def change_label_violet(self):
        self.label.setText('Фиолетовый')
        self.line_edit.setText("#7d00ff")


if __name__ == '__main__':
    main()
