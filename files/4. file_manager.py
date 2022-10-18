#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
 Решите задачу: напишите программу, состоящую из однострочного и многострочного
 текстовых полей и двух кнопок "Открыть" и "Сохранить". При клике на первую должен
 открываться на чтение файл, чье имя указано в поле класса Entry , а содержимое файла
 должно загружаться в поле типа Text .
 При клике на вторую кнопку текст, введенный пользователем в экземпляр Text , должен
 сохраняться в файле под именем, которое пользователь указал в однострочном текстовом
 поле
 Файлы будут читаться и записываться в том же каталоге, что и файл скрипта, если
 указывать имена файлов без адреса.
"""

from PySide2.QtWidgets import (QApplication, QWidget,
                               QPushButton, QLineEdit,
                               QVBoxLayout, QHBoxLayout,
                               QTextEdit, QFileDialog)
import sys


def main():
    app = QApplication(sys.argv)
    window = TextManager()
    window.show()
    sys.exit(app.exec_())


class TextManager(QWidget):
    def __init__(self):
        super().__init__()
        self.inline_edit = QLineEdit('None', self)
        self.text_edit = QTextEdit(self)
        self.open_button = QPushButton('Открыть', self)
        self.save_button = QPushButton('Сохранить', self)

        self.initial_ui()

    def initial_ui(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Текстовый редактор')

        box_layout_parent = QVBoxLayout()
        box_layout_child = QHBoxLayout()
        box_layout_child.addWidget(self.inline_edit)
        box_layout_child.addWidget(self.open_button)
        box_layout_child.addWidget(self.save_button)
        box_layout_parent.addLayout(box_layout_child)
        box_layout_parent.addWidget(self.text_edit)

        self.open_button.clicked.connect(self.open_document)
        self.save_button.clicked.connect(self.save_document)

        self.setLayout(box_layout_parent)

    def open_document(self):
        if self.inline_edit.text() == '':
            file_name, file_type = QFileDialog.getOpenFileName(self)
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read()
            self.text_edit.setText(text)
        else:
            try:
                file_name = self.inline_edit.text()
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read()
                self.text_edit.setText(text)
            except ValueError:
                self.text_edit.setText('Error')

    def save_document(self):
        file_name, file_type = QFileDialog.getSaveFileName(
            self,
            'Select one file to open',
            '',
            'Text files (*.txt)'
        )
        if file_name:
            text_from_file = self.text_edit.toPlainText()
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(text_from_file)
            self.inline_edit.setText(file_name)


if __name__ == '__main__':
    main()
