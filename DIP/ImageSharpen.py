
def grad_img(img):
    # img为ndarray格式
    # 求取一张图片的梯度
    img_x = img.shape[0]
    img_y = img.shape[1]
    img_c = img.shape[2]  # 通道数
    grad = np.zeros((img_x, img_y, img_c))
    # 转换为float
    img_f = img.astype('float')
    grad_f = grad.astype('float')
    for c in range(img_c):
        for x in range(img_x - 1):
            for y in range(img_y - 1):
                gx = abs(img_f[x, y, c] - img_f[x + 1, y, c])  # 水平方向的梯度
                gy = abs(img_f[x, y, c] - img_f[x, y + 1, c])  # 垂直方向的梯度
                grad_f[x, y, c] = gx + gy  # 某像素点的梯度,这里可以通过乘以一个系数进行调整锐度
    img_f = img_f.astype('uint8')
    grad_f = grad_f.astype('uint8')
    return img_f, grad_f
def sharp_img(img):
    img_f, grad_f = grad_img(img)
    sharp_img = grad_f + img_f
    return sharp_img


import cv2
import matplotlib.pyplot as plt
import numpy as np
from THKits import numpy_to_qimage,qimg_to_numpy,img_show_int
if __name__ == '__main__':
    # 加载显示
    path = "../image/lena.png"
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    # img_show_int(img) # 原图显示
    sharp_img = sharp_img(img)
    # img_show_int(sharp_img) # 锐化图片显示
    qimg = numpy_to_qimage(sharp_img)
    # pixmap = qimg_to_pixmap(qimg)
    npimg = qimg_to_numpy(qimg)
    img_show_int(npimg)
    # print(pixmap)


