
# https://yangcha.github.io/iview/iview.html

#for finding points of the image
import cv2 as cv
import numpy as np


img = cv.imread("Resources/warp_pers.jpg")

width,height =200,300 # final image size
pts1=np.float32([[1390,2276],[2261,2219],[1404,3122],[2403,3088]]) # from a html page which is stored in the reading list of
# safari
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(pts1,pts2)
imgOutput = cv.warpPerspective(img,matrix,(width,height))


cv.imshow("Img",img)
cv.imshow("warp Img",imgOutput)
cv.waitKey(0)