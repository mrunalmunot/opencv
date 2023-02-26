import cv2
img = cv2.imread("KK.png")

#Getting rows and cols pixel
rows, cols, _ = img.shape
print("row:",rows, "cols:", cols, "other:", _) #rows and cols are in pixel

# #accessing pixel of image
# pixel = img[100, 100]
# print("pixel: ", pixel)

# #changing value of pixel
# img[100, 100] = [1, 1, 1]

# pixel = img[100, 100]
# print("pixel: ", pixel)

# c = 0
# for i in range(rows):
#     c += 100
#     for j in range(cols-1, -1, -1):
#         img[i, j] = [i, c, j]


# import math
# x = 200
# y = 300
# r = 50

# for i in range(360):
#     x1 = int(r * math.cos(i * math.pi / 180))
#     y1 = int(r * math.sin(i * math.pi / 180))
#     for i in range(x1+x):
#         for j in range(y1+y):
#             img[i, j] = [i, 1, 1]

print("Size of Image: ", img.size)
#cv2.copyMakeBorder(src,top,bottom,left,right,border type)  
#top,bottom,left,right => in pixel
#row: 477 cols: 622
img1 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = [255,0,0] )

cv2.imshow("Knowledge Kida", img1)
cv2.waitKey(20000)
cv2.destroyAllWindows()
