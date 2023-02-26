import cv2

# circle(img, center, radius, color, thickness, linetype, shift)
# thickness if +ve =>outline;  if -ve =>filled circle

img = cv2.imread("media/KK.png")
cv2.circle(img, (150, 150), 100, (255, 0, 0), -1)

cv2.imshow("Knowledge Kida", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
