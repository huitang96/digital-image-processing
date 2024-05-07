
import logging
from PyQt6.QtGui import QImage, QPixmap, QPainter, QTransform
from PyQt6.QtCore import Qt
# 设置日志记录
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# 将滤波器矩阵定义为外部变量，提高代码的可维护性
SHARPEN_MATRIX_DATA = [
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
]

def sharpen_filter(input_pixmap):
    try:
        matrix = build_sharpen_matrix()
        image = convert_to_img(input_pixmap)
        sharpened_image = apply_sharpen_filter(image, matrix)
        output_pixmap = QPixmap.fromImage(sharpened_image)
        return output_pixmap
    except Exception as e:
        logging.error(f"Error during image sharpening: {e}")
        # 根据实际情况，可以选择返回一个错误标记的图像或者None
        return None

def build_sharpen_matrix():
    # 注意这里改为使用QTransform
    transform = QTransform()
    for row in range(3):
        for col in range(3):
            value = SHARPEN_MATRIX_DATA[row][col]
            transform.translate(col, row)  # 移动到当前矩阵位置
            transform.scale(value, value)  # 应用权重作为缩放因子
            transform.translate(-col, -row)  # 移回原点准备下一次操作
    return transform

def convert_to_img(pixmap):
    image = pixmap.toImage()
    return image

def apply_sharpen_filter(image, transform):
    # 使用QTransform代替QMatrix4x4
    sharpened_image = QImage(image.size(), QImage.Format.Format_RGB32)
    painter = QPainter(sharpened_image)
    painter.drawImage(0, 0, image.transformed(transform, Qt.TransformationMode.SmoothTransformation))
    painter.end()
    return sharpened_image
