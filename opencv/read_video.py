import cv2 as cv

cap = cv.VideoCapture("Resources/test.mp4")

while True:
    succes,img = cap.read()
    cv.imshow("video",img)
    if cv.waitKey(1) and 0xFF ==ord('q'):
        break