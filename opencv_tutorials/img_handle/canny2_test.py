#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "
可以在运行时调整阈值大小的程序
使用createTrackbar进行调节
"
author= "huangtw"
ctime = 2017/03/03
"""


import cv2
import numpy as np

def cannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray,(3,3),0)
    detected_edges = cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('canny demo',dst)

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3

img = cv2.imread('../images/0.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('canny demo')


cv2.createTrackbar('Min threshold','canny demo', lowThreshold, max_lowThreshold, cannyThreshold)

cannyThreshold(0)  # initialization
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()