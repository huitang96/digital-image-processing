
from PyQt6.QtCore import Qt

def image_show(pixmap, image_label):
        image_label.setPixmap(pixmap.scaled(
            image_label.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))