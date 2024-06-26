from PyQt6.QtGui import QPixmap, QImage, QColor

def threshold_pixel(pixel_value, threshold):
    if pixel_value > threshold:
        return 255
    else:
        return 0
def image_binarization(pixmap, threshold):
    print("开始二值化操作")
    # 将 QPixmap 转换为 QImage
    image = pixmap.toImage()
    # 将图像转换为灰度格式
    image = image.convertToFormat(QImage.Format.Format_Grayscale8)
    # 定义一个简单的二值化函数，使用固定阈值（此处为127）
    # 遍历图像的每一个像素进行二值化处理
    for x in range(image.width()):
        for y in range(image.height()):
            gray_value = image.pixelColor(x, y).value()  # 获取灰度值
            binary_value = threshold_pixel(gray_value,threshold)  # 计算二值化后的值
            image.setPixelColor(x, y, QColor(binary_value, binary_value, binary_value, 255))  # 设置新像素值
            status_flag = 1
    # 将二值化的 QImage 转换回 QPixmap
    binary_pixmap = QPixmap.fromImage(image)
    return binary_pixmap

