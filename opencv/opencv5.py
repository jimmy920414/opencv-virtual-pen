#---侦测颜色---
import cv2 
import numpy as np 

def empty(v):
    pass
img = cv2.imread('XiWinnie.jpg')
img = cv2.resize(img, (0,0), fx=0.5,fy=0.5)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #将jpg转换hsv



cv2.namedWindow('TrackBar')#创建视窗
cv2.resizeWindow('TrackBar', 640, 320)
    #改变视窗大小 宽640 高320
             
                  #控制条名称，控制条在那个视窗，初始值，最大值，被改变后呼叫的函式
cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)#创建控制条
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)

while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    
    
    mask= cv2.inRange(hsv, lower, upper )
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('img', img)
    # cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.waitKey(1)


