#!/usr/bin/python2.7

#preinstalled modules
import sys
import operator
from common import anorm2, draw_str
from time import clock
import math

#downloaded modules
import numpy as np
import cv2
import cProfile
from matplotlib import pyplot as plt
import pylab as P
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import pepper_det as pep

#user files
import color_filters as FT
import defines as DEF

def main():
    # load grayscale image
    cv2.namedWindow('lines', cv2.WINDOW_NORMAL)
    im = cv2.imread("../gauge2.jpg")
    gray_im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

    # create version to draw on and blurred version
    draw_im = cv2.cvtColor(gray_im, cv2.COLOR_GRAY2BGR)
    blur = cv2.GaussianBlur(gray_im, (0,0), 3)

    m,n = gray_im.shape

    # Hough transform for circles
    #circles = cv2.HoughCircles(gray_im, cv2.HOUGH_GRADIENT, 2, 10, np.array([]), 20, 60, m/10)[0]

    # Hough transform for lines (regular and probabilistic)

    edges = cv2.Canny(blur, 20, 60)
    edges = cv2.threshold(blur, 80, 255, cv2.THRESH_BINARY)[1]
    lines = cv2.HoughLines(edges, 2, np.pi/90, 10)
    plines = cv2.HoughLinesP(edges, 1, np.pi/180, 200,None, 10, 10)

    # draw
    #for c in circles[:1]:
     # green for circles (only draw the 3 strongest)
     #cv2.circle(draw_im, (c[0],c[1]), c[2], (0,255,0), 3)

    for line in lines:
        for (rho, theta) in line:
            # blue for infinite lines (only draw the 5 strongest)
            x0 = np.cos(theta)*rho
            y0 = np.sin(theta)*rho
            pt1 = ( int(x0 + (m+n)*(-np.sin(theta))), int(y0 + (m+n)*np.cos(theta)) )
            pt2 = ( int(x0 - (m+n)*(-np.sin(theta))), int(y0 - (m+n)*np.cos(theta)) )
            cv2.line(draw_im, pt1, pt2, (255,0,0), 3)

    for pline in plines:
        for l in pline:
             # red for line segments
             cv2.line(draw_im, (l[0],l[1]), (l[2],l[3]), (0,0,255), 3)

    #$cv2.imshow("lines", blur)
    cv2.imshow("lines",draw_im)
    cv2.waitKey(0)

    # save the resulting image
    cv2.imwrite("res.jpg",draw_im)


if __name__ == "__main__":
    main()