#---图片转灰阶、模糊，找边缘，膨脹图片 
import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8) #建立二维阵列
kernel1 = np.ones((5,5), np.uint8)

img = cv2.imread('colorcolor.jpg')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #转换灰阶图片
blur = cv2.GaussianBlur(img, (3, 3), 0) #模糊图片
    #高斯模糊函数    要转换的图片,和的大小，标准差
can = cv2.Canny(img, 100 , 150)#找边缘
          #找边缘 图片，最低值，最高值
dilate = cv2.dilate(can, kernel, iterations=1)#膨胀图片
                   #要膨胀的图片 二维阵列 膨胀几次
erode = cv2.erode(dilate, kernel1, iterations=1)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('blur',blur)
cv2.imshow('can',can)
cv2.imshow('dilate',dilate)
cv2.imshow('erode',erode)
cv2.waitKey(0)