#---轮廓检测---
import cv2 

img = cv2.imread('shape.jpg')
imgCon = img.copy()#复制图片
img =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#转灰阶
canny = cv2.Canny(img, 150, 200)#轮廓
#（回传）要找的轮廓,阶层       findContours(要侦测的图片,使用的模式（内外轮廓）,压缩轮廓点)侦测轮廓
contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


for cnt in contours:
    cv2.drawContours(imgCon, cnt, -1, (255,0,0), 4)#画出轮廓(要画的图上,要画的轮廓,要画的轮廓是第几个（都要写-1）,颜色,粗度)
    area = cv2.contourArea(cnt)
    # print(cv2.contourArea(cnt))#找面积
    if area > 500:
        prei = cv2.arcLength(cnt, True)#找边长,是否闭合
        ver = cv2.approxPolyDP(cnt, prei * 0.02, True)#apperoxPolyDP(要近似的轮廓,近似值,是否闭合)近似轮廓的值，回传顶点
        corners = len(ver)
        x, y, w, h = cv2.boundingRect(ver)#图形用方形框起来，回传左上(x,y)宽度以及高度
        cv2.rectangle(imgCon, (x,y), (x+w,y+h), (0, 255, 0), 4 )#cv2.rectangle(要画的图,左上坐标,右下坐标,颜色,粗度)画出方形
        #判断顶点数并写上图形名称
        if corners == 3:
            cv2.putText(imgCon, 'triangle', (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        elif corners == 4:
            cv2.putText(imgCon, 'rectangle', (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        elif corners == 5:
            cv2.putText(imgCon, 'pentagon', (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        elif corners >= 6:
            cv2.putText(imgCon, 'circle', (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)



cv2.imshow('img',img)
cv2.imshow('canny',canny)
cv2.imshow('imgCon',imgCon)
cv2.waitKey(0)