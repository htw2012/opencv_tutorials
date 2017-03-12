#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "
图片缩放
目标：你可以对图像进行倍数的放大和缩小  也可以直接的输入尺寸大小

变换的方法：

CV_INTER_NN - 最近邻插值,

CV_INTER_LINEAR - 双线性插值 (缺省使用)

CV_INTER_AREA - 使用象素关系重采样。当图像缩小时候，该方法可以避免波纹出现。当图像放大时，类似于 CV_INTER_NN 方法..

CV_INTER_CUBIC - 立方插值.
"
author= "huangtw"
ctime = 2017/03/03
"""
import cv2

image=cv2.imread("../images/0.jpg")
res=cv2.resize(image,(32,32),interpolation=cv2.INTER_CUBIC)
cv2.imshow('iker',res)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destoryAllWindows()