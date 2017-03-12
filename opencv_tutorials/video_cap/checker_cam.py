#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
title= "检查摄像头"
author= "huangtw"
ctime = 2017/03/03
"""
import cv2

cam = cv2.VideoCapture(0)
cam.open(0)
results = [ cam.read()[0] for i in range(100) ]
print results