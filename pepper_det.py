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
import color_filters as FT
import defines as DEF

#globals
feature_params = dict( maxCorners = 100, qualityLevel = 0.3, minDistance = 7, blockSize = 7)
lk_params = dict( winSize = (15, 15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))


class App:
    def __init__(self, name, video_src):
        #common
        self.name = name
        global capture
        capture = cv2.VideoCapture(video_src)
        self.cam = capture
        global frame
        _, frame = capture.read()
        global canvas, edges
        canvas = np.zeros_like(frame)
        edges = np.zeros_like(frame)
        global frame_gray
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        self.frame_idx = 0
        #camera movement tracking
        self.track_len = 10
        self.detect_interval = 5

    def next_frame(self):
        global frame, frame_gray, canvas
        _, frame = capture.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canvas = np.zeros_like(frame)

    def video_status(self):
        return capture.isOpened()
        
    def __find_lines(self, edges):
        global canvas
        lines = None
        lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=30,maxLineGap=5)
        if lines is not None:
            for line in lines:
                x1,y1,x2,y2 = line[0]
                cv2.line(canvas,(x1,y1),(x2,y2),DEF.BLUE,2)

    def __find_edges(self, frame):
        global frame_gray
        equilized = np.zeros_like(frame_gray)
        cv2.equalizeHist(frame_gray, equilized)
        edges = cv2.Canny(equilized,10,250,apertureSize = 3)
        dilate_element = cv2.getStructuringElement( cv2.MORPH_ELLIPSE,(3,3))
        edges = cv2.dilate(edges,dilate_element,1)
        #edges = cv2.GaussianBlur(edges, (13,13), 0)
        edges = cv2.bitwise_not(edges)
        edges = cv2.adaptiveThreshold(edges,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,5)
        #edges = cv2.threshold(edges, 150, 200, cv2.THRESH_TRUNC)
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        return edges
    
    class __camera_tracker:
        def __init__(self, frame, prev_gray):
            self.tracks = []
            self.frame = frame
            self.prev_gray = prev_gray
            
        def track_features(self):
            global canvas
            if len(self.tracks) > 0:
                gray0, gray1 = self.prev_gray, cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
                d_x_mean = 0
                d_y_mean = 0
                p0 = np.float32([track[-1] for track in self.tracks]).reshape(-1, 1, 2)
                p1, st, err = cv2.calcOpticalFlowPyrLK(gray0, gray1, p0, None, **lk_params)
                p0r, st, err = cv2.calcOpticalFlowPyrLK(gray1, gray0, p1, None, **lk_params)
                d_abs= abs(p0-p0r).reshape(-1, 2).max(-1)
                d_raw = (p0-p0r).reshape(-1,2).max(-1)
                if (len(d_raw) > 1):
                    d_x_mean = d_raw[0].mean()
                    d_y_mean = d_raw[1].mean()
                good = d_abs < 1
                new_tracks = []
                for tr, (x, y), good_flag in zip(self.tracks, p1.reshape(-1, 2), good):
                    if not good_flag:
                        continue
                    tr.append((x, y))
                    if len(tr) > self.track_len:
                        del tr[0]
                    new_tracks.append(tr)
                    #cv2.circle(canvas, (x, y), 2, DEF.GREEN, -1)
                self.tracks = new_tracks
                #cv2.line(canvas,(x,y), tr[len(tr)-1], DEF.BLUE)
                #cv2.poly
                #cv2.polylines(canvas, [np.int32(tr) for tr in self.tracks], False, DEF.GREEN)
                if (len(self.tracks) > 0):
                    draw_str(canvas, (20, 20), 'track count: %d' % len(self.tracks))
                    draw_str(canvas, (20, 40), 'mean travel: %f' %np.mean(d))
                    draw_str(canvas, (20, 60), 'dX: %f' %d_x_mean)
                    draw_str(canvas, (20, 80), 'dY: %f' %d_y_mean)
                else:
                    cv2.putText(canvas, "lost track", (20, 30), cv2.FONT_HERSHEY_DUPLEX, 1, DEF.RED)
            else:
                canvas = cv2.addWeighted(canvas, 0.3, frame_w_edges, 0.7, 0.0)
            if self.frame_idx % self.detect_interval == 0:
                mask = np.zeros_like(frame_gray)
                mask[:] = 255
                for x, y in [np.int32(tr[-1]) for tr in self.tracks]:
                    #cv2.circle(mask, (x, y), 5, 0, -1)
                    pass
                p = cv2.goodFeaturesToTrack(frame_gray, mask = mask, **feature_params)
                for x, y in np.float32(p).reshape(-1, 2):
                    self.tracks.append([(x, y)])

    def run(self):
            frames = []
            global canvas
            edges = self.__find_edges(frame)
            b,g,r = cv2.split(frame)
            z = np.zeros_like(b)
            o = np.ones_like(b)*255
            #frame_w_canvas = cv2.merge((b,g,r,cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)))
            frame_w_canvas = cv2.bitwise_or(frame, canvas)
            frame_w_edges = cv2.bitwise_and(frame, edges)
            self.frame_idx += 1
            self.prev_gray = frame_gray

            frames = {'original':frame, 'canvas':frame_w_canvas, 'edges':frame_w_edges}
            return frames
            #return mask

    def show_video(self, video_out):
        cv2.imshow(self.name, video_out)

    def close(self):
        capture.release()
        cv2.destroyAllWindows()

class Object:
    x = 0 #these will hold the coordinates of the object "centers". see moments of inertia
    y = 0
    def __init__(self, name="null"):
        self.type = "Object"
        self.color = (0,0,0)
        self.position = 0
        self.area = 0
        if name is "pepper_red":
         self.color = DEF.RED
        if name is "blue":
         self.color = DEF.BLUE

def drawObject(theObjects, frame, contours, hierarchy):
    print("drawObjects")
    #sort objects by x coordinate
    theObjects = (sorted(theObjects, key=operator.attrgetter('x')))

    while (len(theObjects)>0):
        thisObject = theObjects.pop()
        #contours[thisObject.position] = cv2.convexHull(contours[thisObject.position], returnPoints = True)
        #print("last = " + str(len(contours)) + " position = "+str(thisObject.position))
        #if (thisObject.position > (len(contours))):
        #    print("breakpoint")
        cv2.drawContours(frame,contours,thisObject.position, DEF.RED, 5, 5)
        coordinate = (thisObject.x,thisObject.y) #contains coordinates of the object: (int(moment['m10']/area))
        cv2.circle(frame, coordinate, 10, thisObject.color) #draw circle at the object center
        text_org = (thisObject.x+10, thisObject.y)
        if thisObject.color == DEF.RED:
            obj_number = str(len(theObjects))
            cv2.putText(frame, obj_number, text_org, cv2.FONT_HERSHEY_DUPLEX, 1, DEF.WHITE)
        if thisObject.color == DEF.BLUE:
            cv2.putText(frame, "Oreos", text_org, cv2.FONT_HERSHEY_DUPLEX, 1.2, thisObject.color)


def trackFilteredObject(theObject, threshold, HSV, thisFrame):
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
                object.color = theObject.color
                object.position = i
                objects.append(object)
                #print len(objects)
                #print "area is greater than .."
                objectFound = True
              #else: objectFound = False

    assert(len(objects) <= len(contours)), \
        "objects: %d, contours: %d" % (len(objects), len(contours))

    if objectFound is True:
            drawObject(objects,thisFrame,contours,hierarchy)
            #print "supposed to draw"


APP = App("Gothue tracking", "./p2.mp4")


def main():
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 1920/2,1080/2)
    mode = '0'
    paused = False
    red_filter = FT.ColorFilter("red", FT.filter_red)
    while APP.video_status():
        gothue = Object("pepper_red")

        frames = APP.run()
        APP.next_frame()
        hsv, red_threshold = red_filter.apply_filter(frames['original'])

        trackFilteredObject(gothue, red_threshold, hsv, frames['canvas'])


        if mode is '0':
            APP.show_video(frames['original'])
        if mode is '1':
            APP.show_video(frames['canvas'])
        if mode is '2':
            APP.show_video(frames['edges'])
        if mode is '3':
            cv2.imshow(APP.name, cv2.bitwise_and(frames['original'],cv2.cvtColor(red_threshold, cv2.COLOR_GRAY2BGR)))

        key_pressed = cv2.waitKey(1) & 0xFF

        #press m to change display mode
        if key_pressed == ord('m'):
            if mode is '0':
                mode = '1'
            elif mode is '1':
                mode = '2'
            elif mode is '2':
                mode = '3'
            elif mode is '3':
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
            FT.open_trackbar()
    # When everything done, release the capture
    APP.close()

if __name__ == "__main__":
    main()