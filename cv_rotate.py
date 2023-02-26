import cv2

img = cv2.imread("media/KK.png")

#getRotationMatrix2D -> center, angle, scale
#warpAffine -> img, M, (w, h)

(h, w) = img.shape[:2]
center = (w/2, h/2)
angle = 75
scale = 0.2

M = cv2.getRotationMatrix2D(center, angle, scale)
rotate = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Knowledge Kida", rotate)
cv2.waitKey()
cv2.destroyAllWindows()




