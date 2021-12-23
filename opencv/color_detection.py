import cv2 as cv
import numpy as np

def empty(a):
    pass

path = 'Resources/test3.jpg'

# trackbar
cv.namedWindow("Trackbar")
cv.resizeWindow("Trackbar",400,300)

cv.createTrackbar("Hue min","Trackbar",0,179,empty)
cv.createTrackbar("Hue max","Trackbar",179,179,empty)
cv.createTrackbar("Saturation min","Trackbar",0,255,empty)
cv.createTrackbar("Saturation max","Trackbar",255,255,empty)
cv.createTrackbar("Value min","Trackbar",0,255,empty)
cv.createTrackbar("Value max","Trackbar",255,255,empty)


while True:
    img = cv.imread(path)
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    
    h_min= cv.getTrackbarPos("Hue min","Trackbar")
    h_max= cv.getTrackbarPos("Hue max","Trackbar")
    s_min= cv.getTrackbarPos("Saturation min","Trackbar")
    s_max= cv.getTrackbarPos("Saturation max","Trackbar")
    v_min= cv.getTrackbarPos("Value min","Trackbar")
    v_max= cv.getTrackbarPos("Value max","Trackbar")
    
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv.inRange(imgHSV,lower,upper)
    
    imgFinal = cv.bitwise_and(img,img,mask=mask)

    cv.imshow("Img",img)
    cv.imshow("HSV",imgHSV)
    cv.imshow("Mask",mask)
    cv.imshow("final",imgFinal)
    cv.waitKey(1000)
    
    #for red shirt selection
    # h_min = 165
    # h_max =179
    # s_min = 198
    # s_max = 255
    # v_min = 12
    # v_max =183