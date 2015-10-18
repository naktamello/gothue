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
    img1 = cv2.imread('images_to_test/train.png')
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.imread('images_to_test/query_01.png')
    img3 = np.zeros_like(img2)

    # KAZE
    e1_kaze = cv2.getTickCount()
    kaze = cv2.KAZE_create()
    kp_kaze = kaze.detect(img1, None)
    kp_kaze, des_kaze = kaze.compute(img1, kp_kaze)
    #img_kaze = cv2.drawKeypoints(gray, kp_kaze, None, color=(0, 255, 0))
    e2_kaze = cv2.getTickCount()
    time_kaze = (e2_kaze-e1_kaze)/cv2.getTickFrequency()
    print 'KAZE\t' + str(time_kaze) + '\t' + str(time_kaze/len(kp_kaze))
    img_kaze = cv2.drawKeypoints(gray, kp_kaze, None)
    kp1, des1 = kaze.detectAndCompute(img1, None)
    kp2, des2 = kaze.detectAndCompute(img2, None)
    des1 = des1.astype(int)
    des2 = des2.astype(int)
    #orb = cv2.ORB_create()
    #kp1, des1 = orb.detectAndCompute(img1, None)
    #kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key = lambda x:x.distance)


    img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
    plt.imshow(img3)
    plt.show()

    #cv2.imshow('KAZE', img_kaze)
    #cv2.waitKey(0)
    #frame_gray = cv2.Canny(img,100,200)
    #frame_gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY );
    #hist_img = cv2.equalizeHist(img)

    #plt.subplot(121),plt.imshow(img,cmap = 'gray')
    #plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(122),plt.imshow(hist_img,cmap = 'gray')
    #plt.title('equalized'), plt.xticks([]), plt.yticks([])
    #plt.show()

if __name__ == "__main__":
    main()