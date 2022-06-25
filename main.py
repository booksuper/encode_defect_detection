from cv2 import cv2
import numpy as np
from segment import getRoi
from detect import defect_locate

if __name__ == '__main__':
    img = getRoi(r'data1\text1.bmp')
    img_res = defect_locate(img)
    cv2.imwrite('data1\\text1dl_3.bmp',img_res)