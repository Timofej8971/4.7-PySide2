#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Решите задачу: напишите простейший калькулятор, состоящий из двух текстовых полей,
куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/". Результат вычисления
должен отображаться в метке. Если арифметическое действие выполнить невозможно
(например, если были введены буквы, а не числа), то в метке должно появляться слово
"ошибка".
"""

from PySide2.QtWidgets import (QApplication, QWidget,
                               QLabel, QPushButton, QLineEdit, QVBoxLayout)
from PySide2.QtCore import Qt
import sys


class Culculator(QWidget):
    def __init__(self):
        super().__init__()
        self.line_edit_first = QLineEdit(self)
        self.line_edit_second = QLineEdit(self)
        self.button_division = QPushButton('/', self)
        self.button_multiplication = QPushButton('*', self)
        self.button_addition = QPushButton('+', self)
        self.button_subtraction = QPushButton('-', self)
        self.label = QLabel('None', self)

        self.initial_ui()

    def initial_ui(self):
        self.setGeometry(100, 100, 100, 400)
        self.setWindowTitle('Калькулятор')

        box_layout = QVBoxLayout()
        box_layout.addWidget(self.line_edit_first)
        box_layout.addWidget(self.line_edit_second)
        box_layout.addWidget(self.button_addition)
        box_layout.addWidget(self.button_subtraction)
        box_layout.addWidget(self.button_multiplication)
        box_layout.addWidget(self.button_division)
        box_layout.addWidget(self.label)
        self.setLayout(box_layout)

        self.line_edit_first.setAlignment(Qt.AlignCenter)
        self.line_edit_second.setAlignment(Qt.AlignCenter)
        self.label.setAlignment(Qt.AlignCenter)

        self.button_addition.clicked.connect(self.calc_numbers)
        self.button_subtraction.clicked.connect(self.calc_numbers)
        self.button_multiplication.clicked.connect(self.calc_numbers)
        self.button_division.clicked.connect(self.calc_numbers)

    def calc_numbers(self):
        sender = self.sender()
        first_number = float(self.line_edit_first.text())
        second_number = float(self.line_edit_second.text())

        if sender.text() == '+':
            self.label.setText(str(first_number + second_number))

        if sender.text() == '-':
            self.label.setText(str(first_number - second_number))

        if sender.text() == '*':
            self.label.setText(str(first_number * second_number))

        if sender.text() == '/':
            if second_number != 0:
                self.label.setText(str(first_number / second_number))
            else:
                self.label.setText('error')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Culculator()
    window.show()
    sys.exit(app.exec_())
