import cv2 as cv

cap = cv.VideoCapture(0)

cap.set(3,680) # 3 is the id for width of video capture
cap.set(4,480) # 4 is the id for height of video capture
cap.set(10,100) # 10 is the id of brightness of video capture

while True:
    succes,img = cap.read()
    cv.imshow("video",img)
    if cv.waitKey(1) and 0xFF ==ord('q'):
        break