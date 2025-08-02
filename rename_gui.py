import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QFileDialog, QMessageBox, QLineEdit, QHBoxLayout
)

def add_prefix(folder_path, prefix_letter):
    renamed = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            base_name = filename.lstrip(prefix_letter)
            new_name = f'{prefix_letter}{base_name}'

            if new_name != filename:
                new_path = os.path.join(folder_path, new_name)
                os.rename(file_path, new_path)
                renamed.append(f"{filename} → {new_name}")
    return renamed

def remove_prefix(folder_path, letter_to_remove):
    renamed = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path) and filename.startswith(letter_to_remove):
            new_name = filename[len(letter_to_remove):]
            new_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_path)
            renamed.append(f"{filename} → {new_name}")
    return renamed

class RenameApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Переименование файлов")
        self.setMinimumWidth(420)

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Выберите папку и введите буквы:"))

        # Поле для добавления буквы
        add_layout = QHBoxLayout()
        self.letter_add_input = QLineEdit()
        self.letter_add_input.setMaxLength(1)
        self.letter_add_input.setPlaceholderText("Буква для добавления")
        add_layout.addWidget(QLabel("Добавить букву:"))
        add_layout.addWidget(self.letter_add_input)
        layout.addLayout(add_layout)

        # Кнопка добавления
        self.add_button = QPushButton("Добавить букву в начало")
        self.add_button.clicked.connect(self.handle_add)
        layout.addWidget(self.add_button)

        # Поле для удаления буквы
        remove_layout = QHBoxLayout()
        self.letter_remove_input = QLineEdit()
        self.letter_remove_input.setMaxLength(1)
        self.letter_remove_input.setPlaceholderText("Буква для удаления")
        remove_layout.addWidget(QLabel("Удалить букву:"))
        remove_layout.addWidget(self.letter_remove_input)
        layout.addLayout(remove_layout)

        # Кнопка удаления
        self.remove_button = QPushButton("Удалить букву из начала")
        self.remove_button.clicked.connect(self.handle_remove)
        layout.addWidget(self.remove_button)

        self.setLayout(layout)

    def handle_add(self):
        prefix = self.letter_add_input.text().strip()
        if not prefix:
            QMessageBox.warning(self, "Ошибка", "Введите одну букву для добавления.")
            return

        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder_path:
            result = add_prefix(folder_path, prefix)
            if result:
                QMessageBox.information(self, "Готово", "Добавлено:\n" + "\n".join(result))
            else:
                QMessageBox.information(self, "Нет изменений", "Все имена уже корректны.")

    def handle_remove(self):
        letter = self.letter_remove_input.text().strip()
        if not letter:
            QMessageBox.warning(self, "Ошибка", "Введите одну букву для удаления.")
            return

        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку")
        if folder_path:
            result = remove_prefix(folder_path, letter)
            if result:
                QMessageBox.information(self, "Готово", "Удалено:\n" + "\n".join(result))
            else:
                QMessageBox.information(self, "Нет изменений", "Не найдено ни одного файла, начинающегося с этой буквы.")

def main():
    app = QApplication(sys.argv)
    window = RenameApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
