import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),dtype=np.uint8)
# print(img)
#  img[:]=255,0,0 --> converts the whole image into blue


# to draw line
cv.line(img,(0,0),(300,300),(255,0,0),3)
cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # will create a diagonal line all the way to first
# first to corner point

cv.rectangle(img,(0,0),(250,350),(0,0,255)) # this will draw a rectangle on the image
cv.rectangle(img,(0,0),(250,350),(0,0,255),cv.FILLED) # this will draw a rectangle on the image, and fill with that color
cv.circle(img,(256,256),100,(255,255,0),5)

cv.putText(img,"OPEN Computer Vision",(30,500),cv.FONT_HERSHEY_COMPLEX,1,(150,0,9),1)


cv.imshow("Image",img)
cv.waitKey(0)
