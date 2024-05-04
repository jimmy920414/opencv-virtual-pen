#---人臉辨識---
#https://github.com/opencv/opencv/tree/4.x/data/haarcascades
import cv2

img = cv2.imread('qq.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face = cv2.CascadeClassifier('face_detect.xml')#引入模組
faceRect = face.detectMultiScale(gray, 1.1, 5)
#回傳矩形框框，辨識人臉(辨識圖片,縮小的倍數(值越小倍數越小運作時間長),相鄰的框框要有幾個(數值越大越嚴謹可能偵測不准))
print(len(faceRect))

    #矩形框框的左上座標、寬度、高度
for (x, y, w, h) in faceRect:
    cv2.rectangle(img, (x,y), (x+h, y+h), (0,255,0),2)


cv2.imshow('img',img)
cv2.waitKey(0)