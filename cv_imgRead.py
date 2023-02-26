import cv2
#imread
img = cv2.imread("KK.png", 0)
cv2.imshow("Knowledge Kida", img)

cv2.waitKey(30000)
cv2.destroyAllWindows()