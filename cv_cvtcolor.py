import cv2
src = cv2.imread("E:/move22Jan/Screenshot_2022-10-16-13-26-17-58_1c337646f29875672b5a61192b9010f9.jpg")

# new_img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
new_img = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

status = cv2.imwrite("saved2.png", new_img)
if status:
    print("Image written")
else:
    print("Failed!")
cv2.imshow("Knowledge Kida", new_img)
cv2.waitKey(300000)
cv2.destroyAllWindows()