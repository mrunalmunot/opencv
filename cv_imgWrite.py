import cv2
import os
img = cv2.imread("KK.png", 0)
os.chdir("KnowledgeKida")
status = cv2.imwrite("saved2.png", img)
if status:
    print("Image written")
else:
    print("Failed!")