import sys
import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication
from PyQt6.uic import loadUiType
from PyQt6.QtWidgets import QMainWindow
from THKits import pixmap_show, open_file_dialog
from DIP.ImageBinarization import image_binarization
from DIP.EdgeDetection import edge_detection_sobel
from DIP.ImageSharpen import grad_img
from THKits import pixmap_to_qimg, qimg_to_numpy, numpy_to_qimage, qimg_to_pixmap

Ui_MainWindow, _ = loadUiType('./ui/ui.ui')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_10.clicked.connect(self.on_button_10_clicked) # 加载图片
        self.ui.pushButton.clicked.connect(self.on_button_clicked) # 二值化
        self.ui.pushButton_2.clicked.connect(self.on_button_2_clicked) # 边缘检测
        self.ui.pushButton_3.clicked.connect(self.on_button_3_clicked) # 图像锐化

        self.ui.horizontalSlider.valueChanged.connect(self.on_slider_value_changed) # 滑动条
        self.threshold = 127
        self.mode = None
        #设置软件背景图
        # self.ui.label_5.setStyleSheet("border-image: url(./image/background.jpg);")
        self.ui.centralwidget.setStyleSheet("border-image: url(./image/background.jpg);")

    def on_button_10_clicked(self):
        # 加载图片
        try:
            self.file_path = open_file_dialog()
            if self.file_path:
                if os.path.isfile(self.file_path) and os.path.splitext(self.file_path)[1].lower() in ['.png', '.jpg', '.jpeg','.bmp']:
                    self.pixmap = QPixmap(self.file_path)
                    pixmap_show(self.pixmap, self.ui.label_6)
        except Exception as e:
            print(f"Error occurred while opening file dialog: {e}")
    def on_slider_value_changed(self):
        # 获取滑块的值
        if self.mode == "二值化":
            self.threshold = self.ui.horizontalSlider.value()
            self.threshold = int(self.threshold*2.55)
            print("阈值", self.threshold)
        elif self.mode == "边缘检测":
            pass
        elif self.mode == "图像锐化":
            pass
    def on_button_clicked(self):
        # 二值化转换
        self.mode = "二值化"
        if self.ui.label_5.pixmap():
            self.ui.label_5.clear()
        binary_pixmap = image_binarization(self.pixmap, self.threshold)
        pixmap_show(binary_pixmap, self.ui.label_5)
    def on_button_2_clicked(self):
        # 图像锐化
        self.mode = "边缘检测"
        if self.ui.label_5.pixmap():
            self.ui.label_5.clear()
        edge_pixmap = edge_detection_sobel(self.pixmap)
        pixmap_show(edge_pixmap, self.ui.label_5)
    def on_button_3_clicked(self):

        # 图像锐化
        self.mode = "图像锐化"
        if self.ui.label_5.pixmap():
            self.ui.label_5.clear()
        qimg = pixmap_to_qimg(self.pixmap) # pixmap -> qimg
        npimg = qimg_to_numpy(qimg) # qimg -> npimg
        img_f, grad_f = grad_img(npimg) # 求图像梯度
        sharpen_npimg = img_f + grad_f # 计算锐化
        qimg_f = numpy_to_qimage(sharpen_npimg) # npimg -> qimg
        pixmap_f = qimg_to_pixmap(qimg_f) # qimg - >pixmap
        pixmap_show(pixmap_f, self.ui.label_5)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序实例
    window = MainWindow()  # 创建窗口实例
    window.show()
    sys.exit(app.exec())