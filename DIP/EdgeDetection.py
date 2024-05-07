from PyQt6.QtGui import QImage, QPixmap, qRgb, qGray, QPainter, QPen, QBrush, QRadialGradient
from PyQt6.QtCore import Qt, QPoint, qAbs
def sobel_filter(image):
    width, height = image.width(), image.height()
    sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    # canny 算子
    # canny_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    # canny_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    output_image = QImage(width, height, QImage.Format.Format_RGB32)
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            gx = gy = 0
            for i in range(3):
                for j in range(3):
                    pixel = image.pixel(x + i - 1, y + j - 1)
                    gray = qGray(pixel)
                    gx += gray * sobel_x[i][j]
                    gy += gray * sobel_y[i][j]
            gradient_magnitude = qAbs(gx) + qAbs(gy)
            gradient_magnitude = int(gradient_magnitude)
            output_image.setPixel(x, y, qRgb(gradient_magnitude, gradient_magnitude, gradient_magnitude))
    return output_image
def edge_detection_sobel(input_pixmap):
    print("开始边缘检测操作")
    # 将 QPixmap 转换为 QImage
    input_image = input_pixmap.toImage()
    # 使用 Sobel 滤波器计算边缘强度图
    edge_image = sobel_filter(input_image)
    # 将边缘强度图转换回 QPixmap
    output_pixmap = QPixmap.fromImage(edge_image)
    return output_pixmap

# 写一个图像锐化的函数

