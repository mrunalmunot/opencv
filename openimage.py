# Today Showing Image from PC
import cv2
# reading image
img = cv2.imread("images/kk.png")

# displaying image in Output window
cv2.imshow("Output", img)

# display image for infinite time
cv2.waitKey(0)
