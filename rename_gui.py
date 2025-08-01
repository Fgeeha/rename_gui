import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QPushButton, QFileDialog, QMessageBox, QLineEdit, QHBoxLayout
)

def rename_files(folder_path, prefix_letter):
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

class RenameApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Переименование файлов")
        self.setMinimumWidth(400)

        layout = QVBoxLayout()

        self.label = QLabel("Выберите папку и укажите букву:")
        layout.addWidget(self.label)

        # Блок для ввода буквы
        letter_layout = QHBoxLayout()
        self.letter_input = QLineEdit()
        self.letter_input.setMaxLength(1)
        self.letter_input.setPlaceholderText("Введите букву")
        letter_layout.addWidget(QLabel("Буква:"))
        letter_layout.addWidget(self.letter_input)
        layout.addLayout(letter_layout)

        # Кнопка выбора папки
        self.button = QPushButton("Выбрать папку")
        self.button.clicked.connect(self.select_folder)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def select_folder(self):
        prefix_letter = self.letter_input.text().strip()

        if not prefix_letter or len(prefix_letter) != 1:
            QMessageBox.warning(self, "Ошибка", "Введите одну букву для добавления в начало имени.")
            return

        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку с файлами")
        if folder_path:
            result = rename_files(folder_path, prefix_letter)
            if result:
                QMessageBox.information(self, "Готово", "Переименовано:\n" + "\n".join(result))
            else:
                QMessageBox.information(self, "Нет изменений", "Все имена уже корректны.")

def main():
    app = QApplication(sys.argv)
    window = RenameApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
