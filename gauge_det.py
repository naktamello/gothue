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
    img1 = cv2.imread('images_to_test/positives/0037_0139_0049_0153_0153.jpg')
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gauge_cascade = cv2.CascadeClassifier('images_to_test/positives/cascade.xml')
    gauges = gauge_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in gauges:
        cv2.rectangle(img1, (x,y), (x+w, y+h), (255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img1[y:y+h, x:x+w]
    cv2.imshow('img', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()