import cv2 as cv


img = cv.imread("Resources/test.jpg")


cv.imshow("output img",img)
cv.waitKey(0)  # 0 for infinite time,  1 for 1 milisec , 2 for 2 milsec