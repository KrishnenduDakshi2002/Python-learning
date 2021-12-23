import cv2 as cv
import numpy as np

img = cv.imread("Resources/test.jpg")
# defining kernel for cv.dialate()
kernel = np.ones((5,5),dtype=np.uint8)


imggray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imggray,(7,7),0)

imgCanny = cv.Canny(img,110,200)
imgDialation = cv.dilate(imgCanny,kernel,iterations=2)
imgErode = cv.erode(imgDialation,kernel,iterations=3)
cv.imshow("gray image",imggray)
cv.imshow("blur img",imgBlur)
cv.imshow("canny img",imgCanny)
cv.imshow("dialate img",imgDialation)
cv.imshow("erode img",imgErode)
cv.waitKey(0)