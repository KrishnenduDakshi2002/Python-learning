import cv2 as cv
import numpy as np
def empty(a):
    pass

cv.namedWindow("Trackbars")
# cv.resizeWindow("Trackbars",640,240)
cv.createTrackbar("hue min","Trackbars",0,179,empty)
cv.createTrackbar("sat min","Trackbars",0,255,empty)
cv.createTrackbar("val min","Trackbars",0,255,empty)
cv.createTrackbar("hue max","Trackbars",179,179,empty)
cv.createTrackbar("sat max","Trackbars",255,255,empty)
cv.createTrackbar("val max","Trackbars",255,255,empty)
while True:
    img = cv.imread("Resources/test2.jpg")
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    h_min=cv.getTrackbarPos("hue min","Trackbars")
    s_min = cv.getTrackbarPos("sat max","Trackbars")
    print(h_min,s_min)

    cv.imshow("Img",img)
    cv.imshow("ImgHSV",imgHSV)
    cv.waitKey(1000)

