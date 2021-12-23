import cv2 as cv

img = cv.imread("Resources/test.jpg")
print(img.shape)

imgResize = cv.resize(img,(500,1000)) #(width,height)
print(imgResize.shape)


imgCrop = img[0:303,200:500] #(height,width)

cv.imshow("output img",img)
cv.imshow("rsize img",imgResize)
cv.imshow("crop img",imgCrop)
cv.waitKey(0)