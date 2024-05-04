# ---创建图片 切割图片---

import cv2
import numpy as np
import random

img = cv2.imread('colorcolor.jpg')
# img = np.empty((300, 300, 3), np.uint8) 创建图片
# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)] 
newimg = img[:150,200:400]

cv2.imshow('img',img)
cv2.imshow('newimg',newimg)
cv2.waitKey(0)