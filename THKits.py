import numpy as np


def pixmap_show(pixmap, image_label):
    # 图像显示，输入pixmap格式，现在在qt的image_label上
    from PyQt6.QtCore import Qt
    image_label.setPixmap(pixmap.scaled(
        image_label.size(),
        Qt.AspectRatioMode.KeepAspectRatio,
        Qt.TransformationMode.SmoothTransformation))
def open_file_dialog():
    # 打开图片选择对话框
    import os
    from PyQt6.QtWidgets import QFileDialog
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    dialog.setNameFilter("Image files (*.png *.jpg *.jpeg *.bmp)")
    if dialog.exec() == QFileDialog.DialogCode.Accepted:
        file_path = dialog.selectedFiles()[0]
        if os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower() in ['.png', '.jpg', '.jpeg', '.bmp']:
            return file_path

# ======================== QT中几种图片格式转换 ========================
def numpy_to_qimage(img):
    # note: 通过cv.imread读取进来的图片为numpy格式的数据
    from PyQt6.QtGui import QImage
    """Converts a NumPy array to a QImage."""
    if img.shape[2] == 4:  # RGBA
        qimage_format = QImage.Format.Format_RGBA8888
    elif img.shape[2] == 3:  # RGB
        qimage_format = QImage.Format.Format_RGB888
    else:
        raise ValueError("图片的通道数不支持")
    height, width, channel = img.shape
    bytes_per_line = channel * width # 每一行像素所占的字节数
    image_data = img.data.tobytes()
    return QImage(image_data, width, height, bytes_per_line, qimage_format)
def qimg_to_pixmap(qimg):
    # 传入QImage格式的img，返回pixmap格式的img
    from PyQt6.QtGui import QPixmap
    output_pixmap = QPixmap.fromImage(qimg)
    return output_pixmap
def pixmap_to_qimg(input_pixmap):
    input_image = input_pixmap.toImage()
    return input_image
def qimg_to_numpy(qimage):
    from PyQt6.QtGui import QImage
    import numpy as np
    """ Converts a QImage to a numpy array."""
    # 获取图像的宽度、高度和格式
    width = qimage.width()
    height = qimage.height()
    format = qimage.format()
    # 确保QImage的格式为RGB32或RGBA8888，如果不是，可以先转换格式
    if format != QImage.Format.Format_RGB32 and format != QImage.Format.Format_RGBA8888:
        qimage = qimage.convertToFormat(QImage.Format.Format_RGB32 if format == QImage.Format.Format_RGB888 else QImage.Format.Format_RGBA8888)
    # 获取图像的字节数据
    buffer = qimage.bits().asstring(width * height * 4)  # 假设最大可能是32位数据，包括alpha
    # 将字节数据转换为numpy数组
    img_array = np.frombuffer(buffer, dtype=np.uint8).reshape(height, width, -1)
    # 如果原图是RGB没有alpha通道，需要去掉最后一个通道
    if format == QImage.Format.Format_RGB32:
        img_array = img_array[:, :, :3]
    return img_array

def image_show(path):
    import cv2
    import matplotlib.pyplot as plt

    img = cv2.imread(path, cv2.IMREAD_COLOR)
    cv2.imshow("img", img)
    cv2.waitKey()
def img_show_int(img):
    import matplotlib.pyplot as plt
    # 此时img为ndarray格式
    plt.imshow(img)
    plt.title('img')
    plt.show()

def rgb_to_gray(path):
    # RGB转为灰度图
    import cv2
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img_gray
import cv2
img_gray = rgb_to_gray("./image/lena.png")
cv2.imshow("img_gray", img_gray)
cv2.waitKey()
def gray_hist():
    img_gray = rgb_to_gray("./image/lena.png")
    width, height = img_gray.shape[0], img_gray.shape[1]
    max_gray = np.max(img_gray)
    min_gray = np.min(img_gray)
    # 初始化一个字典来存储每个灰度级的频率
    gray_level_freq = {i: 0 for i in range(256)}
    for i in range(width):
        for j in range(height):
            gray_value = img_gray[i, j]
            # 更新该灰度值的频率
            gray_level_freq[gray_value] += 1
    return gray_level_freq

# gray_level_freq = gray_hist()
# gray_level_list = []
# freq_list = []
# for gray_level, freq in gray_level_freq.items():
#     print(f"灰度级 {gray_level}: 出现次数 {freq}")
#     gray_level_list.append(gray_level)
#     freq_list.append(freq)
#
# import matplotlib.pyplot as plt
# plt.plot(gray_level_list, freq_list)
# plt.show()



