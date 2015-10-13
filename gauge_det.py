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
    img = cv2.imread('pressure_gauge_cropped.jpeg',0)
    #frame_gray = cv2.Canny(img,100,200)
    #frame_gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY );
    hist_img = cv2.equalizeHist(img)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(hist_img,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()