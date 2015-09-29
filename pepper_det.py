#!/usr/bin/python2.7

#preinstalled modules
import sys
import operator
from common import anorm2, draw_str
from time import clock

#downloaded modules
import numpy as np
import cv2

#user files
import color_filters
import defines as DEF

feature_params = dict( maxCorners = 100, qualityLevel = 0.3, minDistance = 7, blockSize = 7)
lk_params = dict( winSize = (15, 15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

class App:
    def __init__(self, video_src):
        self.track_len = 10
        self.detect_interval = 5
        self.tracks = []
        self.cam = cap
        self.frame_idx = 0

    def run(self, frame, frame_to_draw):
            frames = []
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame_copy = frame_to_draw.copy()
            vis = frame.copy()
            edges = cv2.Canny(frame_gray,50,150,apertureSize = 3)
            edges = cv2.bitwise_not(edges)
            edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

            frame_copy = cv2.addWeighted(frame_copy, 0.5, edges, 0.5, 0.0)

            if len(self.tracks) > 0:
                img0, img1 = self.prev_gray, frame_gray
                d_x_mean = 0
                d_y_mean = 0
                p0 = np.float32([tr[-1] for tr in self.tracks]).reshape(-1, 1, 2)
                p1, st, err = cv2.calcOpticalFlowPyrLK(img0, img1, p0, None, **lk_params)
                p0r, st, err = cv2.calcOpticalFlowPyrLK(img1, img0, p1, None, **lk_params)
                d = abs(p0-p0r).reshape(-1, 2).max(-1)
                d_raw = (p0-p0r).reshape(-1,2).max(-1)
                if (len(d_raw) > 1):
                    d_x_mean = d_raw[0].mean()
                    d_y_mean = d_raw[1].mean()
                good = d < 1
                new_tracks = []
                for tr, (x, y), good_flag in zip(self.tracks, p1.reshape(-1, 2), good):
                    if not good_flag:
                        continue
                    tr.append((x, y))
                    if len(tr) > self.track_len:
                        del tr[0]
                    new_tracks.append(tr)
                    cv2.circle(frame_to_draw, (x, y), 2, DEF.GREEN, -1)
                self.tracks = new_tracks
                #cv2.line(frame_to_draw,(x,y), tr[len(tr)-1], DEF.BLUE)
                #cv2.poly
                cv2.polylines(frame_to_draw, [np.int32(tr) for tr in self.tracks], False, DEF.GREEN)
                frame_to_draw = cv2.addWeighted(frame_to_draw, 0.3, frame_copy, 0.7, 0.0)
                if (len(self.tracks) > 0):
                    draw_str(frame_to_draw, (20, 20), 'track count: %d' % len(self.tracks))
                    draw_str(frame_to_draw, (20, 40), 'mean travel: %f' %np.mean(d))
                    draw_str(frame_to_draw, (20, 60), 'dX: %f' %d_x_mean)
                    draw_str(frame_to_draw, (20, 80), 'dY: %f' %d_y_mean)
                else:
                    cv2.putText(frame_to_draw, "lost track", (20, 30), cv2.FONT_HERSHEY_DUPLEX, 1, DEF.RED)
            else:
                frame_to_draw = cv2.addWeighted(frame_to_draw, 0.3, frame_copy, 0.7, 0.0)
            if self.frame_idx % self.detect_interval == 0:
                mask = np.zeros_like(frame_gray)
                mask[:] = 255
                for x, y in [np.int32(tr[-1]) for tr in self.tracks]:
                    cv2.circle(mask, (x, y), 5, 0, -1)
                p = cv2.goodFeaturesToTrack(frame_gray, mask = mask, **feature_params)
                if p is not None:
                    for x, y in np.float32(p).reshape(-1, 2):
                        self.tracks.append([(x, y)])


            self.frame_idx += 1
            self.prev_gray = frame_gray
            #cv2.imshow('lk_track', frame_to_draw)

            frames = (frame_to_draw, edges)
            return frames
            #return mask


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
            cv2.putText(frame, obj_number, text_org, cv2.FONT_HERSHEY_DUPLEX, 1, DEF.WHITE)
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
cap = cv2.VideoCapture("./p4.mp4") #putting '0' tries to load the default cam on the machine
opflow = App("0")

# main #
def main():
  cv2.namedWindow('object_discovered', cv2.WINDOW_NORMAL)
  cv2.resizeWindow('object_discovered', 1920/2,1080/2)
  color_filters.color_filter_init()
  mode = '0'
  paused = False
  while (cap.isOpened()):
    if paused == False:
        _, frame = cap.read()
        orig_frame = frame.copy()
        # Capture frame-by-frame
        #_, frame = cap.read()
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
        b = cv2.addWeighted(threshold_red_opened, 0.7, b, 0.3, 0.1)
        g = cv2.addWeighted(threshold_red_opened, 0.7, g, 0.3, 0.1)
        r = cv2.addWeighted(threshold_red_opened, 0.7, r, 0.3, 0.1)
        frame = cv2.merge((b,g,r))

        frames = opflow.run(orig_frame, frame)
        #cv2.add(vis, frame, frame)
        #cv2.imshow('object_discovered', frame)

    if mode is '0':
        cv2.imshow('frame',frames[0])
    if mode is '1':
        cv2.imshow('frame', frames[1])
    if mode is '2':
        cv2.imshow('frame', frame)

    key_pressed = cv2.waitKey(1) & 0xFF

    #press m to change display mode
    if key_pressed == ord('m'):
        if mode is '0':
            mode = '1'
        elif mode is '1':
            mode = '2'
        elif mode is '2':
            mode = '0'
    #press p for pause
    if key_pressed == ord('p'):
        paused = not(paused)
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