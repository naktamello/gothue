#!/usr/bin/python2.7

import cv2

cv2.namedWindow("lll")
cap = cv2.VideoCapture("./harvesting.mp4")
while( cap.isOpened() ) :
    ret,img = cap.read()
    cv2.imshow("lll",img)
    k = cv2.waitKey(10)
    if k == 27:
        breakn("./harvesting.mp4")