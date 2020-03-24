from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2

from config import *

# load the example image
image = cv2.imread("test.jpg")

# pre-process the image by resizing it, 
# converting it to grayscale, blurring it,
# and computing an edge map
image = imutils.resize(image, height=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 1: Localize the LCD
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)
# cv2.imwrite("step1_result.png", edged)
if DEBUG == True:
	cv2.imshow("Step 1 result", edged)
	cv2.waitKey(0)

# Step 2: Extract the LCD
# find contours in the edge map, then sort them by their area
# in descending order
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
displayCnt = None

# loop over the contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	# if the contour has 4 vertices, then we have found
	# the thermostat display
	if len(approx) == 4:
		displayCnt = approx
		break

# extract the thermostat display, apply a perspective transform to it
warped = four_point_transform(gray, displayCnt.reshape(4, 2))
output = four_point_transform(image, displayCnt.reshape(4, 2))
# cv2.imwrite("step2_result.png", output)
if DEBUG == True:
	cv2.imshow("Step 2 Result", output)
	cv2.waitKey(0)

# Step 3: Extract the Digits from the LCD
# threshold the warped image, then apply a series of morphological
# operations to cleanup the thresholded image
thresh = cv2.threshold(warped, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

if DEBUG == True:
	cv2.imshow("Morphological result", thresh)
	cv2.waitKey(0)

# find contours in the thresholded image, then initialize the digit contours lists
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
digitCnts = []

# loop over the digit area candidates
for c in cnts:
	# compute the bounding box of the contour
	(x, y, w, h) = cv2.boundingRect(c)

	# if the contour is sufficiently large, it must be a digit
	if w >= 15 and (h >= 30 and h <= 40):
		digitCnts.append(c)

		new_output = cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv2.imwrite("step3_result.png", new_output)
if DEBUG == True:
	cv2.imshow("Step 3 result", new_output)
	cv2.waitKey(0)
