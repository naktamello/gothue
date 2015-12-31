#!/usr/bin/python2.7
import cv2
import numpy as np
filter_red = {'tone0':{'lowb' : [0,200,0], 'upb' : [19,255,255]}, 'tone1':{'lowb' : [160,100,50], 'upb' : [179,255,255]}, 'weight': 0.5}
filter_blue = {'tone0':{'lowb' : [5,100,100], 'upb' : [10,255,255]}, 'tone1':{'lowb' : [90,100,100], 'upb' : [137,255,255]}, 'weight': 0.0}


class ColorFilter:
    def __init__(self, color, filter):
        self.color = color
        self.settings = filter
        print ("filter preset = " + str(self.settings))

    def open_image(self, thresh):
        #create structuring element that will be used to "dilate" and "erode" image.
        #the element chosen here is a 3px by 3px rectangle
        erodeElement = cv2.getStructuringElement( cv2.MORPH_ELLIPSE,(3,3))
        #dilate with larger element so make sure object is nicely visible
        dilateElement = cv2.getStructuringElement( cv2.MORPH_ELLIPSE,(8,8))
        thresh = cv2.erode(thresh,erodeElement,2)
        thresh = cv2.dilate(thresh,dilateElement,2)
    
        return thresh

    def apply_filter(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #add color ranges as a weighted sum (tones of the same color) (i.e. crimson vs slight orange tint)
        tone0 = cv2.inRange(hsv, np.array(self.settings['tone0']['lowb']), np.array(self.settings['tone0']['upb']))
        tone1 = cv2.inRange(hsv, np.array(self.settings['tone1']['lowb']), np.array(self.settings['tone1']['upb']))
        threshold = cv2.addWeighted(tone0, float(self.settings['weight']), tone1, float(1.0-self.settings['weight']), 0.0)
        threshold = cv2.GaussianBlur(threshold, (5,5), 0 )
        #morphoOps erodes & dilates sequentially to "open" the previously filtered hsv image
        threshold = self.open_image(threshold)
        threshold = cv2.threshold(threshold, 127, 255, cv2.THRESH_BINARY)[1]
        return hsv, threshold

def open_trackbar():
    global list_of_filters
    list_of_filters = []
    list_of_filters.append(red)
    list_of_filters.append(blue)

    for i in range(0, len(list_of_filters)):
        this_filter = list_of_filters[i]
        cv2.namedWindow(str(this_filter.color), cv2.WINDOW_AUTOSIZE)
        cv2.resizeWindow(str(this_filter.color), 480,360)
        for x in range (0, len(np.array(this_filter.settings['tone0']['lowb']))):
            trackbar_name = 'lower_lowb' + str(x)
            this_array = np.array(this_filter.settings['tone0']['lowb'])
            cv2.createTrackbar(trackbar_name, str(this_filter.color), 0, 255, trackbar_callback)
            cv2.setTrackbarPos(trackbar_name, str(this_filter.color), this_array[x])
        for x in range (0, len(np.array(this_filter.settings['tone0']['upb']))):
            trackbar_name = 'lower_upb' + str(x)
            this_array = np.array(this_filter.settings['tone0']['upb'])
            cv2.createTrackbar(trackbar_name, str(this_filter.color), 0, 255, trackbar_callback)
            cv2.setTrackbarPos(trackbar_name, str(this_filter.color), this_array[x])
        for x in range (0, len(np.array(this_filter.settings['tone1']['lowb']))):
            trackbar_name = 'upper_lowb' + str(x)
            this_array = np.array(this_filter.settings['tone1']['lowb'])
            cv2.createTrackbar(trackbar_name, str(this_filter.color), 0, 255, trackbar_callback)
            cv2.setTrackbarPos(trackbar_name, str(this_filter.color), this_array[x])
        for x in range (0, len(np.array(this_filter.settings['tone1']['upb']))):
            trackbar_name = 'upper_upb' + str(x)
            this_array = np.array(this_filter.settings['tone1']['upb'])
            cv2.createTrackbar(trackbar_name, str(this_filter.color), 0, 255, trackbar_callback)
            cv2.setTrackbarPos(trackbar_name, str(this_filter.color), this_array[x])



def trackbar_callback(x):
    pass
    #l1 = cv2.getTrackbarPos('lower_1', str(list_of_filters[i].color))


