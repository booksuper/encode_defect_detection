#检测镂空缺陷
from cv2 import cv2
import numpy as np
#读取图像
o=cv2.imread(r'data2\text9.bmp') 
#将原图转为单通道的灰度图像
gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
#创建drawcontour函数需要的模板
#mask=np.zeros(gray.shape,np.uint8)
#将图像二值化
t,binary=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#创建图像副本
copy_1=binary.copy()
#创建第一个闭操作所需核函数
kernel=np.ones((30,30),np.uint8)
#创建第二个闭操作所需核函数
kernel2=np.ones((50,50),np.uint8)
#将原图副本进行第一次闭操作，定位缺口的位置
close=cv2.morphologyEx(copy_1,cv2.MORPH_CLOSE,kernel)
#将原图副本进行第二次闭操作，得到与操作的操作图像
close2=cv2.morphologyEx(copy_1,cv2.MORPH_CLOSE,kernel2)
#将第一次操作得到的图像反二值化
s,binary_inv=cv2.threshold(close,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

s=cv2.bitwise_and(close2,binary_inv)
cv2.imwrite(r'data2\text9Gap_30_50.bmp',s)
#cv2.imwrite(r'date of GetRoiSecond\text1opening_150.bmp',opening)


# contours,hierarchy=cv2.findContours(binary_inv,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# n=len(contours)
# print(n)
# a=[]
# b=0
# for i in range(n):
    
#     a.append(cv2.contourArea(contours[i]))
# min=a[0]
# for i in range(n):
#     if a[i]<min:
#         min=a[i]
#         b=i
# mask=cv2.drawContours(mask,contours,b,(255,255,255),-1)