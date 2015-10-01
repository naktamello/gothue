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

        cv2.namedWindow(name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(name, 1920/2,1080/2)

        global capture
        capture = cv2.VideoCapture(video_src)
        self.cam = capture

        global frame
        _, frame = capture.read()
        global prev_frame
        prev_frame = frame
        global frame_gray
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        global prev_gray
        prev_gray = frame_gray

        global canvas, edges
        canvas = np.zeros_like(frame)
        edges = np.zeros_like(frame)

        global gothue, red_filter
        gothue = Object("pepper_red")
        red_filter = FT.ColorFilter("red", FT.filter_red)

        self.frame_idx = 0
        #camera movement tracking
        self.track_len = 10
        self.detect_interval =4
        self.camera_tracker = self.__camera_tracker(self)

    def next_frame(self):
        global frame, frame_gray, prev_gray, canvas
        prev_frame = frame
        _, frame = capture.read()
        prev_gray = frame_gray
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        canvas = np.zeros_like(frame)
        self.frame_idx += 1

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
        def __init__(self, app):
            self.tracks = []
            self.detect_interval = app.detect_interval
            global frame
            self.p_frame = np.zeros_like(frame)
            self.p_threshold = np.zeros_like(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
            self.kp_pairs = None
            self.kp = None
            self.kp_prev = None
            self.des = None
            self.des_prev = None
            self.matches = None
            self.dist = None
            self.avg_dis =[]
            self.mean = [0,0]

        def draw_arrow(self, canvas, origin):
            angle = math.atan2(self.mean[1],self.mean[0]) - math.pi/4
            mag = math.sqrt(math.pow(self.mean[1],2) + math.pow(self.mean[0],2) )
            width = int(1*mag)
            length = int(5*mag)
            print("mag = %f angle = %f" % (mag, angle))
            head_width = int(width *2.2)
            head_length = int(width *2)
            x = origin[0]
            y = origin[1]
            rot = np.asarray([[np.cos(angle), -np.sin(angle)],[np.sin(angle), np.cos(angle)]], np.float32)
            print(rot)
            top_left = [-length/2, width/2]
            top_right = [length/2, width/2]
            bottom_left = [-length/2, -width/2]
            bottom_right = [length/2, -width/2]
            arrow_head_0 = [length/2, head_width/2]
            arrow_head_1 = [length/2 + head_length, 0]
            arrow_head_2 = [length/2, -head_width/2]
            top_left = np.dot(rot, top_left).astype(int) + origin
            top_right = np.dot(rot, top_right).astype(int) + origin
            bottom_left = np.dot(rot, bottom_left).astype(int) + origin
            bottom_right = np.dot(rot, bottom_right).astype(int) + origin
            arrow_head_0 = np.dot(rot, arrow_head_0).astype(int) + origin
            arrow_head_1 = np.dot(rot, arrow_head_1).astype(int) + origin
            arrow_head_2 = np.dot(rot, arrow_head_2).astype(int) + origin
            polygon = [top_left, top_right, bottom_left, bottom_right]
            #polygon = np.array(polygon, np.int32)
            #polygon = polygon.reshape((-1,1,2))
            #line = [[polygon[0],polygon[1]]]
            cv2.line(canvas, tuple(top_left), tuple(top_right), DEF.GREEN,3)
            cv2.line(canvas, tuple(bottom_left), tuple(bottom_right), DEF.GREEN,3)
            cv2.line(canvas, tuple(top_left), tuple(bottom_left), DEF.GREEN,3)
            cv2.line(canvas, tuple(top_right), tuple(arrow_head_0), DEF.GREEN,3)
            cv2.line(canvas, tuple(bottom_right), tuple(arrow_head_2), DEF.GREEN, 3)
            cv2.line(canvas, tuple(arrow_head_0), tuple(arrow_head_1), DEF.GREEN, 3)
            cv2.line(canvas, tuple(arrow_head_1), tuple(arrow_head_2), DEF.GREEN, 3)
            #cv2.polylines(canvas, polygon, False, DEF.RED)
            pass

        def track_features(self, this_frame, frame_idx, threshold, canvas):
            threshold = None
            self.draw_arrow(canvas, (1920/2,200))
            if frame_idx%self.detect_interval == 0:
                orb = cv2.ORB_create()
                self.kp = orb.detect(this_frame, threshold)
                self.kp_prev = orb.detect(self.p_frame, self.p_threshold)
                self.kp, self.des = orb.compute(this_frame, self.kp)
                self.kp_prev, self.des_prev = orb.compute(self.p_frame, self.kp_prev)
                self.p_frame = this_frame
                self.p_threshold = threshold
                bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
                if self.des_prev is not None:
                    self.matches = bf.match(self.des, self.des_prev)
                    self.dist = [m.distance for m in self.matches]
                    thresh_dist = (sum(self.dist)/len(self.dist))*0.5
                    self.dist = [m for m in self.matches if m.distance < thresh_dist]
                if len(self.avg_dis) > 0 and self.matches:
                    self.mean = [np.mean(self.avg_dis[0]), np.mean(self.avg_dis[1])]
            if self.kp and self.kp_prev:
                #cv2.drawKeypoints(canvas,self.kp_prev,canvas,DEF.GREEN,0)
                #cv2.drawKeypoints(canvas,self.kp,canvas,DEF.BLUE,0)
                pass
            if self.matches:
                self.avg_dis = []
                for m in self.dist:
                    prev_p = (int(self.kp_prev[m.trainIdx].pt[0]), int(self.kp_prev[m.trainIdx].pt[1]))
                    this_p = (int(self.kp[m.queryIdx].pt[0]), int(self.kp[m.queryIdx].pt[1]))
                    self.avg_dis.append([(prev_p[0]-this_p[0]), (prev_p[1]-this_p[1])])
                    #cv2.line(canvas, prev_p, this_p, DEF.BLUE, 5)


    def run(self):
            frames = []
            global frame, prev_frame, prev_gray, canvas, red_filter, gothue
            hsv, red_threshold = red_filter.apply_filter(frame)
            edges = self.__find_edges(frame)
            canvas_copy=canvas.copy()
            trackFilteredObject(gothue, red_threshold, hsv, canvas)
            self.camera_tracker.track_features(frame, self.frame_idx, red_threshold, canvas)

            frame_w_fruit = cv2.bitwise_and(frame,cv2.cvtColor(red_threshold, cv2.COLOR_GRAY2BGR))
            frame_w_canvas = cv2.bitwise_or(frame, canvas)
            #frame_w_canvas = canvas
            frame_w_edges = cv2.bitwise_and(frame, edges)

            frames = {'original':frame,'fruit':frame_w_fruit, 'canvas':frame_w_canvas, 'edges':frame_w_edges}
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





#########################################################
#########################################################
APP = App("Gothue tracking", "./p4.mp4")

def main():
    mode = '0'
    paused = False

    while APP.video_status():
        if not paused:
            frames = APP.run()

            APP.next_frame()

            if mode is '0':
                APP.show_video(frames['original'])
            if mode is '1':
                APP.show_video(frames['fruit'])
            if mode is '2':
                APP.show_video(frames['canvas'])
            if mode is '3':
                APP.show_video(frames['edges'])

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