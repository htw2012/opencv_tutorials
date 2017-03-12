#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= ""
author= "huangtw"
ctime = 2017/03/03
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('../images/0.jpg')
# grayImage = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh1=cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
ret,thresh2=cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY_INV)
ret,thresh3=cv2.threshold(grayImage, 127, 255, cv2.THRESH_TRUNC)
ret,thresh4=cv2.threshold(grayImage, 127, 255, cv2.THRESH_TOZERO)
ret,thresh5=cv2.threshold(grayImage, 127, 255, cv2.THRESH_TOZERO_INV)
titles = ['Gray Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [grayImage, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in xrange(6):
   plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
   plt.title(titles[i])
   plt.xticks([]),plt.yticks([])
plt.show()