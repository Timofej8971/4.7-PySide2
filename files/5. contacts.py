#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Напишите программу, в которой имеется несколько объединенных в группу радиокнопок,
индикатор которых выключен ( indicatoron=0 ). Если какая-нибудь кнопка включается, то в
метке должна отображаться соответствующая ей информация. Обычных кнопок в окне быть
не должно.

"""

from PySide2.QtWidgets import (QWidget, QButtonGroup,
                               QApplication, QPushButton,
                               QGridLayout, QLabel)
from PySide2.QtCore import Qt
import sys


def main():
    app = QApplication(sys.argv)
    window = Contacts()
    window.show()
    sys.exit(app.exec_())


class Contacts(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.radio_button_1 = QPushButton('Скорая')
        self.radio_button_2 = QPushButton('Полиция')
        self.radio_button_3 = QPushButton('Пожарные')
        self.group = QButtonGroup()
        self.grid = QGridLayout()
        self.contacts = {
            'Скорая': '103',
            'Полиция': '102',
            'Пожарные': '101'
        }

        self.initial_ui()

    def initial_ui(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Телефонная книга")
        self.label.setAlignment(Qt.AlignCenter)

        self.radio_button_1.setCheckable(True)
        self.radio_button_2.setCheckable(True)
        self.radio_button_3.setCheckable(True)
        self.group.addButton(self.radio_button_1)
        self.group.addButton(self.radio_button_2)
        self.group.addButton(self.radio_button_3)
        self.group.buttonClicked.connect(self.action)

        self.grid.setSpacing(10)
        self.grid.addWidget(self.radio_button_1, 1, 0)
        self.grid.addWidget(self.radio_button_2, 2, 0)
        self.grid.addWidget(self.radio_button_3, 3, 0)
        self.grid.addWidget(self.label, 2, 2)
        self.setLayout(self.grid)

    def action(self, butn):
        self.label.setText(self.contacts[butn.text()])


if __name__ == '__main__':
    main()
