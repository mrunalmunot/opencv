import cv2
img = cv2.imread("media/KK.png")

#putText(img, "text", (pt), font, scale, color, thickness)

cv2.putText(img, "Please Like Share and Subscribe!", (40, 45), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (255, 0, 0), 2)

cv2.imshow("Knowledge Kida", img)

cv2.waitKey()
cv2.destroyAllWindows()