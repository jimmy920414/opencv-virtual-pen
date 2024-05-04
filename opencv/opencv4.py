#---圖片上畫線、方形、圓形，在圖片上寫字
import cv2
import numpy as np 

img = np.zeros((600, 600, 3), np.uint8)

cv2.line(img, (0, 0),(img.shape[1], img.shape[0]),(0, 255, 0), 2)#划线
        #要画线的图片，开始的点，结束的点，颜色，粗度 （img.shape[1]图片的宽度，img.shape[0]图片的高度）
cv2.rectangle(img, (0, 0), (400, 300), (0, 0, 255),  cv2.FILLED)#画方 （cv2.FILLED填满方形）
cv2.circle(img, (300,400), 30, (255,0,0),  cv2.FILLED)#画⚪
                #圆形中心点
cv2.putText(img, 'hello', (100,500), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)#写文字
                 #要写的字，文字坐标，文字字体，文字大小，文字颜色，文字粗细





cv2.imshow('img',img)
cv2.waitKey(0)