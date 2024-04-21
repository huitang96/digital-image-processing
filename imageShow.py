import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

def image_show(imagePath, image_label):
    if os.path.isfile(imagePath) and os.path.splitext(imagePath)[1].lower() in ['.png', '.jpg', '.jpeg', '.bmp']:
        pixmap = QPixmap(imagePath)
        image_label.setPixmap(pixmap.scaled(
            image_label.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))