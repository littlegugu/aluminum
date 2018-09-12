import os
import cv2
os.chdir("D:\\project\\aluminum\\data1")

im = cv2.imread("1.jpg")  #读取图片
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)   #转换了灰度化
# im_gray.axis("off")
# im_gray.title("Input Image")
# im_gray.imshow(im_gray, cmap="gray")  #显示图片
# im_gray.show()
# cv2
# cv2.imshow("1",im_gray)
# cv2.waitKey(10000)
cv2.waitKey (0)  
cv2.imwrite("cat2.jpg", im_gray)
cv2.destroyAllWindows() 