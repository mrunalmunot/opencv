import cv2

img = cv2.imread("media/KK.png")

# rectangle(img, ptr1, ptr2, color, thickness, linetype, shift)

cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), -15)

cv2.imshow("Knowledge Kida", img)

cv2.waitKey(0)
cv2.destroyAllWindows()