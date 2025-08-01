import os
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QPushButton, QFileDialog, QMessageBox
)

def rename_files(folder_path):
    renamed = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            base_name = filename.lstrip('к')
            new_name = f'к{base_name}'

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

        self.label = QLabel("Нажмите кнопку, чтобы выбрать папку с файлами:")
        layout.addWidget(self.label)

        self.button = QPushButton("Выбрать папку")
        self.button.clicked.connect(self.select_folder)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Выбери папку")
        if folder_path:
            result = rename_files(folder_path)
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
