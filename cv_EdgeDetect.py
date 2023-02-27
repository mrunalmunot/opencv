import cv2

#Canny => path, minVal, maxVal, aperture, L2gradient

img = cv2.imread("media/KK.png")
edge = cv2.Canny(img, 100, 200)

cv2.imshow("Knowledge Kida Original", img)
cv2.imshow("Knowledge Kida Edge Detected", edge)

cv2.waitKey()
cv2.destroyAllWindows()