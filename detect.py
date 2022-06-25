from cv2 import cv2
import numpy as np
def defect_locate(in_img):

    img3=in_img.copy()
    gray=cv2.cvtColor(in_img,cv2.COLOR_BGR2GRAY)
    ret,binary=cv2.threshold(gray,220,255,cv2.THRESH_BINARY)
    img=binary.copy()
    img2=binary.copy()
    contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    s=[]
    n=len(contours)
    print(n)
    kernel=np.ones((50,50),np.uint8)
    close=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
    M=cv2.moments(close)
    center_x=int(M["m10"]/M["m00"])
    center_y=int(M["m01"]/M["m00"])
    print(center_x)
    print(center_y)
    img3=cv2.circle(img3,(center_x,center_y),15,(0,0,255),-1)

    for i in range(n):
        s.append(cv2.contourArea(contours[i]))

    # for i in range(n):
    #     print(s[i])
    sum1=sum(s)
    k=sum1/n

    for i in range(n):
        cnt=contours[i]
        topmost=tuple(cnt[cnt[:,:,1].argmin()][0])
        bottommost=tuple(cnt[cnt[:,:,1].argmax()][0])
        y1=topmost[1]
        y2=bottommost[1]
        if y1<center_y and y2<center_y:
            if s[i]<k:
                # print(i)
                # print(s[i])
                if abs(y1-center_y)<abs(y2-center_y):
                    img3=cv2.circle(img3,topmost,70,(0,0,255),3)
                else:
                    img3=cv2.circle(img3,bottommost,70,(0,255,0),3)
                return img3

                cv2.imwrite('data1\\text1dl.bmp',img3) 
        else:
            if s[i]<k:
                # print(i)
                # print(s[i])
                if abs(y1-center_y)<abs(y2-center_y):
                    img3=cv2.circle(img3,bottommost,70,(0,0,255),3)
                else:
                    img3=cv2.circle(img3,topmost,70,(0,255,0),3)
                return img3

                cv2.imwrite('data1\\text1dl_2.bmp',img3)