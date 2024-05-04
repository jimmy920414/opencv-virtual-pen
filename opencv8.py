#   虛擬筆
import cv2
import numpy as np

#侦测轮廓的数值
contourPen = [[107, 109, 81, 130, 255, 102],
              [102, 255, 0, 155, 255, 35]]
#设置颜色
penColor = [[255, 0, 0],
            [255, 255, 255]]

#[x, y, color]
drawPoints = []


#偵測顏色
def findpen(img):

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
    for i in range(len(contourPen)):
        lower = np.array(contourPen[i][:3])
        upper = np.array(contourPen[i][3:6])
    
        mask= cv2.inRange(hsv, lower, upper )
        result = cv2.bitwise_and(img, img, mask=mask)
        penx, peny =findContour(mask)
        cv2.circle(imgCon, (penx, peny), 10, penColor[i], cv2.FILLED)
        if peny != -1:
            drawPoints.append([penx, peny, i])
    # cv2.imshow('result',result)

#輪廓偵測
def findContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1, -1, -1, -1
    for cnt in contours:
        # cv2.drawContours(imgCon, cnt, -1, (0,255,0), 4)
        area = cv2.contourArea(cnt)
        if area > 500:
            prei = cv2.arcLength(cnt, True)
            ver = cv2.approxPolyDP(cnt, prei * 0.02, True)
            x, y, w, h = cv2.boundingRect(ver)

    return  x+w//2, y

def draw(drawpoints):
    for point in drawpoints:
        cv2.circle(imgCon, (point[0], point[1]), 10, penColor[point[2]], cv2.FILLED)

       
#讀取鏡頭
cap = cv2.VideoCapture(1)
while True:
    ret,frame = cap.read()
    if ret :
        imgCon = frame.copy()
        cv2.imshow('video',frame)
        findpen(frame)
        draw(drawPoints)
        cv2.imshow('contour',imgCon)
    else:
        break

    if cv2.waitKey(1) == ord('q'):
        break