#!/usr/bin/python2.7

#preinstalled modules
import sys
import operator

#downloaded modules
import numpy as np
import cv2

#user files
import color_filters
import defines as DEF

class Object:
    x = 0 #these will hold the coordinates of the object "centers". see moments of inertia
    y = 0
    def __init__(self, name="null"):
        self.type = "Object"
        self.Color = (0,0,0)
        self.position = 0
        self.area = 0
        if name is "blue":
         #self.HSVmin = (92, 0, 0)
         #self.HSVmax = (124, 256, 256)
         self.Color = DEF.BLUE
        if name is "red":
         #self.HSVmin = (0, 200, 0)
         #self.HSVmax = (19, 255, 255)
         self.Color = DEF.RED

def drawObject(theObjects, frame, temp, contours, hierarchy):
    theObjects = (sorted(theObjects, key=operator.attrgetter('x')))

    while (len(theObjects)>0):
        thisObject = theObjects.pop()
        #contours[thisObject.position] = cv2.convexHull(contours[thisObject.position], returnPoints = True)
        #print("last = " + str(len(contours)) + " position = "+str(thisObject.position))
        #if (thisObject.position > (len(contours))):
        #    print("breakpoint")
        cv2.drawContours(frame,contours,thisObject.position, thisObject.Color,5,5)
        coordinate = (thisObject.x,thisObject.y) #contains coordinates of the object: (int(moment['m10']/area))
        cv2.circle(frame, coordinate, 10, thisObject.Color) #draw circle at the object center
        text_org = (thisObject.x+10, thisObject.y)
        if thisObject.Color == DEF.RED:
            obj_number = str(len(theObjects))
            cv2.putText(frame, obj_number, text_org, cv2.FONT_HERSHEY_DUPLEX, 1, color_filters.COLOR_YELLOW)
        if thisObject.Color == DEF.BLUE:
            cv2.putText(frame, "Oreos", text_org, cv2.FONT_HERSHEY_DUPLEX, 1.2, thisObject.Color)

def morphOps(thresh):
    #create structuring element that will be used to "dilate" and "erode" image.
    #the element chosen here is a 3px by 3px rectangle
    erodeElement = cv2.getStructuringElement( cv2.MORPH_ELLIPSE,(3,3))
    #dilate with larger element so make sure object is nicely visible
    dilateElement = cv2.getStructuringElement( cv2.MORPH_ELLIPSE,(8,8))
    thresh = cv2.erode(thresh,erodeElement,2)
    thresh = cv2.dilate(thresh,dilateElement,2)

    return thresh

def trackFilteredObject(theObject, threshold, HSV, cameraFeed):
    temp = threshold.copy()
    objects = []
    _, contours, hierarchy = cv2.findContours(temp, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    objectFound = False
    #print hierarchy
    if contours is not None and len(contours) > 0:
        numObjects = len(contours)
        #print("objects = %d" % numObjects )
        if numObjects<1024:
            for i in range (0, len(contours)):
              moment = cv2.moments(contours[i])
              area = moment['m00']
              if area > DEF.AREA:
                #print("area = %d" % area)
                object = Object()
                object.area = area
                object.x = int(moment['m10']/area)
                object.y = int(moment['m01']/area)
                object.type = theObject.type
                object.Color = theObject.Color
                object.position = i
                objects.append(object)
                #print len(objects)
                #print "area is greater than .."
                objectFound = True
              #else: objectFound = False

    assert(len(objects) <= len(contours)), \
        "objects: %d, contours: %d" % (len(objects), len(contours))

    if objectFound is True:
            drawObject(objects,cameraFeed,temp,contours,hierarchy)
            #print "supposed to draw"


# global variables #
cap = cv2.VideoCapture("./p3.mp4") #putting '0' tries to load the default cam on the machine

# main #
def main():
  cv2.namedWindow('object_discovered', cv2.WINDOW_NORMAL)
  cv2.resizeWindow('object_discovered', 1920/2,1080/2)
  color_filters.color_filter_init()

  while (cap.isOpened()):
    # Capture frame-by-frame
    _, frame = cap.read()
    blue = Object("blue")
    red = Object("red")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    #add color ranges as a weighted sum (tones of the same color) (i.e. crimson vs slight orange tint)
    lower_red_hue_range = cv2.inRange(hsv, np.array(color_filters.red.filter_settings['lower']['lowb']), np.array(color_filters.red.filter_settings['lower']['upb']))
    upper_red_hue_range = cv2.inRange(hsv, np.array(color_filters.red.filter_settings['upper']['lowb']), np.array(color_filters.red.filter_settings['upper']['upb']))
    threshold_red = cv2.addWeighted(lower_red_hue_range, float(color_filters.red.filter_settings['weight']), upper_red_hue_range, float(1.0-color_filters.red.filter_settings['weight']), 0.0)
    threshold_red = cv2.GaussianBlur(threshold_red, (5,5), 0 )
    #morphoOps erodes & dilates sequentially to "open" the previously filtered hsv image
    threshold_red_opened = morphOps(threshold_red)
    threshold_red_opened = cv2.threshold(threshold_red_opened, 127, 255, cv2.THRESH_BINARY)[1]
    trackFilteredObject(red, threshold_red_opened, hsv, frame)

    lower_blue_hue_range = cv2.inRange(hsv, np.array(color_filters.blue.filter_settings['lower']['lowb']), np.array(color_filters.blue.filter_settings['lower']['upb']))
    upper_blue_hue_range = cv2.inRange(hsv, np.array(color_filters.blue.filter_settings['upper']['lowb']), np.array(color_filters.blue.filter_settings['upper']['upb']))
    threshold_blue = cv2.addWeighted(lower_blue_hue_range, float(color_filters.blue.filter_settings['weight']), upper_blue_hue_range, float(1.0-color_filters.blue.filter_settings['weight']), 0.0)
    threshold_blue_opened = morphOps(threshold_blue)
    trackFilteredObject(blue, threshold_blue_opened, hsv, frame)

    #split channels then add filtered threshold (binary image) to the original
    #this is done so that we can see how well the filter is working
    b,g,r = cv2.split(frame)
    b = cv2.addWeighted(threshold_red_opened, 0.8, b, 0.2, 0.1)
    g = cv2.addWeighted(threshold_red_opened, 0.8, g, 0.2, 0.1)
    r = cv2.addWeighted(threshold_red_opened, 0.8, r, 0.2, 0.1)
    frame = cv2.merge((b,g,r))
    cv2.imshow('object_discovered', frame)

    #cv2.imshow('frame',threshold_red)
    key_pressed = cv2.waitKey(1) & 0xFF

    #press p for pause
    if key_pressed == ord('p'):
        while (1):
            key_pressed = cv2.waitKey(1) & 0xFF
            if key_pressed == ord('p'):
                break
    #press q to close the program
    if key_pressed == ord('q'):
        break
    #press t to enable trackbars for filters (not working yet)
    if key_pressed == ord('t'):
        print "trackbar"
        color_filters.open_trackbar()

  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
    main()