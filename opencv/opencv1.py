# ----------读取图片----------
# cv2.imread()读取图片
# cv2.imshow(x,y) 显示图片 x=视窗标题 y=要显示的图片 
# cv2.waitkey(x) 延迟 x为时间（毫秒）
# cv2.reasize(x,(y,y))改变大小 y为要改变的大小
# ----------读取影片----------
# cap.vidocaputer() 读取影片
# cv2.imshow(x,y) 显示影片 
# cv2.waitkey(x) 延迟 x为时间（毫秒）
# 

import cv2 


cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    frame = cv2.resize(frame,(0,0),fx=0.4,fy=0.4)
    if ret :
        cv2.imshow('video',frame)
    else:
        break

    if cv2.waitKey(10) == ord('q'):
        break


