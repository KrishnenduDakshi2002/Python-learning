import cv2 as cv
import numpy as np

img = cv.imread("Resources/test.jpg")

imgHor= np.hstack((img,img))
imgVer= np.vstack((img,img))

cv.imshow("Horizontal img",imgHor)
cv.imshow("vertical img",imgVer)

cv.waitKey(0)