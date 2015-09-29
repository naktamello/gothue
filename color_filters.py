#!/usr/bin/python2.7
import cv2
import numpy as np
filter_red = {'lower':{'lowb' : [0,200,0], 'upb' : [19,255,255]}, 'upper':{'lowb' : [160,100,50], 'upb' : [179,255,255]}, 'weight': 0.5}
filter_blue = {'lower':{'lowb' : [5,100,100], 'upb' : [10,255,255]}, 'upper':{'lowb' : [90,100,100], 'upb' : [137,255,255]}, 'weight': 0.0}

COLOR_YELLOW = (255, 255, 255)

class ColorFilter:
    def __init__(self, color, filter):
        self.color = color
        self.filter_settings = filter


def color_filter_init():
    global red
    red = ColorFilter('red', filter_red)
    print ("red filter preset = " + str(red.filter_settings))
    global blue
    blue= ColorFilter('blue', filter_blue)
    print ("blue filter preset = " + str(blue.filter_settings))
    print("initializing color_filters")

def open_trackbar():
    global list_of_filters
    list_of_filters = []
    list_of_filters.append(red)
    list_of_filters.append(blue)

    for i in range(0, len(list_of_filters)):
        this_filter = list_of_filters[i]
        cv2.namedWindow(str(this_filter.color), cv2.WINDOW_AUTOSIZE)
        cv2.resizeWindow(str(this_filter.color), 480,360)
        for x in range (0, len(np.array(this_filter.filter_settings['lower']['lowb']))):
            trackbar_name = 'lower_lowb' + str(x)
            this_array = np.array(this_filter.filter_settings['lower']['lowb'])
            cv2.createTrackbar(trackbar_name, str(this_filter.color), 0, 255, trackbar_callback)
            cv2.setTrackbarPos(trackbar_name, str(this_filter.color), this_array[x])
        for x in range (0, len(np.array(this_filter.filter_settings['lower']['upb']))):
            trackbar_name = 'lower_upb' + str(x)
            this_array = np.array(this_filter.filter_settings['lower']['upb'])
            cv2.createTrackbar(trackbar_name, str(this_filter.color), 0, 255, trackbar_callback)
            cv2.setTrackbarPos(trackbar_name, str(this_filter.color), this_array[x])
        for x in range (0, len(np.array(this_filter.filter_settings['upper']['lowb']))):
            trackbar_name = 'upper_lowb' + str(x)
            this_array = np.array(this_filter.filter_settings['upper']['lowb'])
            cv2.createTrackbar(trackbar_name, str(this_filter.color), 0, 255, trackbar_callback)
            cv2.setTrackbarPos(trackbar_name, str(this_filter.color), this_array[x])
        for x in range (0, len(np.array(this_filter.filter_settings['upper']['upb']))):
            trackbar_name = 'upper_upb' + str(x)
            this_array = np.array(this_filter.filter_settings['upper']['upb'])
            cv2.createTrackbar(trackbar_name, str(this_filter.color), 0, 255, trackbar_callback)
            cv2.setTrackbarPos(trackbar_name, str(this_filter.color), this_array[x])



def trackbar_callback(x):
    pass
    #l1 = cv2.getTrackbarPos('lower_1', str(list_of_filters[i].color))


