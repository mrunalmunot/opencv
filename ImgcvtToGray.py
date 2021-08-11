import cv2
img = cv2.imread("images/kk.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Normal Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)
