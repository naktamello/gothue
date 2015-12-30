#!/usr/bin/python2.7
import sys
import numpy as np
import cv2
import defines as DEF

def make_line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

class Object:
    x = 0 #these will hold the coordinates of the object "centers". see moments of inertia
    y = 0
    def __init__(self, name="null"):
        self.type = "Object"
        self.color = DEF.RED
        self.position = 0
        self.area = 0

def main():
    # parameters
    file = "./test.jpg"
    draw = True
    hough_circle = True
    hough_line = True
    hough_pline = False
    do_canny = False
    do_blur = True
    do_threshold = True
    do_contours = True
    window_name = 'gauge'
    line_thickness = 2

    # setup
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    im = cv2.imread(file)
    gray_im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    canvas = np.zeros_like(im)  # output image
    blank = np.zeros_like(im)
    np.copyto(canvas, im)
    prep = gray_im  # copy of grayscale image to be preprocessed for angle detection
    height, width = gray_im.shape
    mask = np.zeros_like(prep)
    scale_factor = 1.15

    # preprocessing image:
    if do_blur:
        prep = cv2.GaussianBlur(prep, (3, 3), 2, 2)
    if do_canny:
        prep = cv2.Canny(prep, 20, 60)
    if do_threshold:
        # create structuring element that will be used to "dilate" and "erode" image.
        # the element chosen here is a 3px by 3px rectangle
        prep = cv2.adaptiveThreshold(prep, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,25,3)
        #prep = cv2.threshold(prep, 50, 255, cv2.THRESH_BINARY_INV)[1]
        erodeElement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        # dilate with larger element so make sure object is nicely visible
        dilateElement = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))
        prep = cv2.erode(prep, erodeElement, 2)
        prep = cv2.dilate(prep, dilateElement, 1)

    # Hough transforms (circles, lines, plines)
    if hough_circle:
        # HoughCircles returns output vector (x,y,radius) inside an one element list so [0] is appended at the end
        circles = cv2.HoughCircles(gray_im, cv2.HOUGH_GRADIENT, 2, 10, None, param1=50, param2=30, minRadius=height / 10,
                                   maxRadius=0, )[0]
        if circles is None:
            sys.exit("could not locate the gauge circle")  # if no circles are found terminate the program here
        else:
            # use only gauge image that is inside the first circle found
            for c in circles[:1]:
                # scale factor makes applicable area slightly larger just to be safe we are not missing anything
                cv2.circle(mask, (c[0], c[1]), int(c[2] * scale_factor), (255, 255, 255), -1)
                # mask=cv2.threshold(mask, 128, 255,cv2.THRESH_BINARY)
                prep = cv2.bitwise_and(prep, mask)

    if do_contours:
        objects = []
        copy = np.zeros_like(prep)  # output image
        np.copyto(copy, prep)
        _, contours, hierarchy = cv2.findContours(copy, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
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
                    object.position = i
                    objects.append(object)
                    #print len(objects)
                    #print "area is greater than .."
                    objectFound = True
                  #else: objectFound = False

        assert(len(objects) <= len(contours)), \
            "objects: %d, contours: %d" % (len(objects), len(contours))
        while (len(objects)>0):
            thisObject = objects.pop()
            #contours[thisObject.position] = cv2.convexHull(contours[thisObject.position], returnPoints = True)
            cv2.drawContours(blank,contours,thisObject.position, DEF.WHITE, 5, 2)


    if hough_line:
        blank = cv2.cvtColor(blank, cv2.COLOR_BGR2GRAY)
        lines = cv2.HoughLines(blank, 1, np.pi / 90, 50)
    if hough_pline:
        plines = cv2.HoughLinesP(prep, 1, np.pi / 180, 20, None, minLineLength = height/10, maxLineGap = 1)

    first = True
    for c in circles[:1]:
        # green for circles (only draw the 3 strongest)
        cv2.circle(canvas, (c[0], c[1]), c[2], (0, 255, 0), line_thickness)
        # cv2.circle()
        # res = cv2.bitwise_and(frame,frame, mask= mask)
        if first:
            first = False
            circle_x = c[0]
            circle_y = c[1]
            radius = int(c[2])
    first = True
    needle_lines = []
    angles = []
    for line in lines[:2]:
        for (rho, theta) in line:
            # blue for infinite lines (only draw the 5 strongest)
            x0 = np.cos(theta) * rho
            y0 = np.sin(theta) * rho
            pt1 = (int(x0 + (height + width) * (-np.sin(theta))), int(y0 + (height + width) * np.cos(theta)))
            pt2 = (int(x0 - (height + width) * (-np.sin(theta))), int(y0 - (height + width) * np.cos(theta)))
            cv2.line(canvas, pt1, pt2, (255, 0, 0), line_thickness)
            needle_lines.append(make_line(pt1,pt2))
            angles.append(theta)
            i += 1
            if first:
                first = False
                line_x = x0
                line_y = y0
                #angle = 90 - (theta * 360 / (2 * np.pi))
                line_mask = np.zeros_like(mask)
                rect_height = int(radius / 4)
                rect_width = int(radius * 2)
                cv2.line(line_mask, pt1, pt2, (255, 255, 255),
                         rect_height)  # mask width is quarter of circle radius found above
                mask = cv2.bitwise_and(mask, line_mask)
                M = cv2.getRotationMatrix2D((x0, y0), (theta * 360 / (2 * np.pi)) - 90, 1)
    avg_theta = (angles[0] + angles[1])/2
    angle = ((avg_theta * 360 / (2 * np.pi)))
    if angle > 360.0:
        angle -= 360
    assert(len(needle_lines) >= 2)
    R = intersection(needle_lines[0], needle_lines[1])
    if R:
        print "Intersection detected:", R
        cv2.circle(canvas, R, 10, DEF.RED, 3)
    else:
        print "No single intersection point detected"
    prep = cv2.bitwise_and(prep, mask)
    density = cv2.warpAffine(prep, M, (width, height))
    density_rect_width = radius * 2
    if density_rect_width % 2 is not 0:
        density_rect_width -= 1
    density_rect_height = rect_height / 3
    if density_rect_height % 2 is not 0:
        density_rect_height -= 1
    density_rect_origin_x = int(line_x - density_rect_width / 2)
    density_rect_origin_y = int(line_y - density_rect_height / 2)
    density_rect = np.zeros(shape=(density_rect_height, density_rect_width)).astype(np.uint8)
    for i, row in enumerate(density_rect):
        for j, pixel in enumerate(row):
            density_rect[i, j] = density[density_rect_origin_y + i, density_rect_origin_x + j]
    left, right = np.hsplit(density_rect, 2)
    left_density = 0
    right_density = 0
    for row in left:
        for pixel in row:
            if pixel:
                left_density += 1
    for row in right:
        for pixel in row:
            if pixel:
                right_density += 1
    if left_density > right_density:
        pass
        #angle += 180

    cv2.putText(canvas, "angle:" + str(angle), (int(height * 0.4), int(width * 0.6)), cv2.FONT_HERSHEY_PLAIN, 2, (200, 50, 0), 3)

    if hough_pline:
        for pline in plines[:10]:
            for l in pline:
                # red for line segments
                cv2.line(canvas, (l[0], l[1]), (l[2], l[3]), (0, 0, 255), line_thickness)

    if draw:
        canvas = np.concatenate((im, canvas), axis=1)
        cv2.imshow(window_name, canvas)
    else:
        cv2.imshow(window_name, prep)
    cv2.waitKey(0)

    # save the resulting image
    if draw:
        cv2.imwrite("res.jpg", canvas)

    f = open('./gauge_angle.txt', 'w')
    f.write("angle:" + str(angle) + "\width")
    f.close()


if __name__ == "__main__":
    main()
