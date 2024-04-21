import os
from PyQt6.QtWidgets import QFileDialog

def open_file_dialog():
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    dialog.setNameFilter("Image files (*.png *.jpg *.jpeg *.bmp)")

    if dialog.exec() == QFileDialog.DialogCode.Accepted:
        file_path = dialog.selectedFiles()[0]
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower() in ['.png', '.jpg', '.jpeg', '.bmp']:
            print(file_path)
            return file_path



