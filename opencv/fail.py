import cv2 as cv
def empty(a):
    pass
cv.namedWindow("test")
cv.createTrackbar("test no","test",100,200,empty)
cv.createTrackbar("test no1","test",101,201,empty)
cv.createTrackbar("test no2","test",102,202,empty)
cv.createTrackbar("test no3","test",103,203,empty)
img = cv.imread("Resources/test2.jpg")
# cv.imshow("output",img)
while True:
    tn=cv.getTrackbarPos("test no","test")
    tn1=cv.getTrackbarPos("test no1","test")
    tn2=cv.getTrackbarPos("test no2","test")
    tn3=cv.getTrackbarPos("test no3","test")
    print(tn,tn1,tn2,tn3)
    cv.waitKey(1)