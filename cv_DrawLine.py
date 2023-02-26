import cv2

#line(img, pt1, pt2, color, thinkness, linetype, shift)

img = cv2.imread("media/KK.png")
cv2.line(img, (10, 10), (200, 200), (0, 0, 0). 20)

cv2.imshow("Knowledge Kida", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

