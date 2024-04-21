import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.uic import loadUiType

from pathChoose import open_file_dialog
from imageShow import image_show
from PyQt6.QtWidgets import QMainWindow

Ui_MainWindow, _ = loadUiType('./ui.ui')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_10.clicked.connect(self.on_button_10_clicked)

    def on_button_10_clicked(self):
        try:
            file_path = open_file_dialog()
            if file_path:
                image_show(file_path, self.ui.label_5)
        except Exception as e:
            print(f"Error occurred while opening file dialog: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序实例
    window = MainWindow()  # 创建窗口实例
    window.show()
    sys.exit(app.exec())