#!/usr/bin/python

import cv2
import numpy as np
BLUE = (255, 0, 0)
def __find_lines(edges):
    global im
    lines = None
    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=5,maxLineGap=5)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(im,(x1,y1),(x2,y2),BLUE,2)

# Read image
im = cv2.imread("gauge_upclose.png", cv2.IMREAD_GRAYSCALE)
threshold = cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,3)
__find_lines(threshold)
#hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

# Show keypoints
cv2.imshow("gauge", threshold)
cv2.waitKey(0)
