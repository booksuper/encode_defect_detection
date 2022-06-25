from cv2 import cv2
import numpy as np
def getRoi(path):
    #读取图像
    o=cv2.imread(r'data1\text1.bmp') 
    #创建空模板，为后面画轮廓做准备
    mask=np.zeros(o.shape,np.uint8)
    #将原图转为单通道的灰度图像
    gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)
    #获得最佳阈值t
    t,otsu=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #将灰度图像二值化
    ret,binary=cv2.threshold(gray,t,255,cv2.THRESH_BINARY)
    #创建图像副本
    copy_1=binary.copy()
    #创建闭操作所需核函数
    kernel=np.ones((50,50),np.uint8) 
    #将原图副本进行闭操作处理
    close=cv2.morphologyEx(copy_1,cv2.MORPH_CLOSE,kernel, iterations=1)
    #获得二值图的各个轮廓
    contours,hierarchy=cv2.findContours(close,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    l=len(contours)
    #创建一个空列表用来装各个轮廓面积值
    a=[]
    #将面积值装入空列表中
    for i in range(l):
        a.append(cv2.contourArea(contours[i]))
    #初始化面积最大值max和面积最大时的轮廓索引号n
    max=a[0]
    n=0
    #找出面积最大时的轮廓索引号n
    for j in range(l):
        if a[j]>max:
            max=a[j]
            n=j
    #创建roi模板。注意，此处不可直接将contours【n】与原图相与，因为他们大小，类型都不一致，会报错！此处或许有更简便的方法。
    mask=cv2.drawContours(mask,contours,n,(255,255,255),-1)
    #模板是rgb图像，要将其转为单通道的灰度图像，否则与操作将会报错！！！
    mask_gray=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    #利用与操作获得roi区域,此处特别注意原图需要为灰度图像，若是用二值化图像，则会出现操作之后的图片比原图稍微大一点的现象！！！
    s=cv2.bitwise_and(gray,mask_gray)
    res = cv2.cvtColor(s,cv2.COLOR_GRAY2BGR)
    return res
    #保存图片
    cv2.imwrite(r'data1\text1roi.bmp',s)
    print("成功获取roi图像")