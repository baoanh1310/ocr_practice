# USAGE
# python contours.py --image circle.png

import cv2 
import numpy as np 
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)

# In OpenCV, finding contours is like finding white object from black background. 
# So remember, object to be found should be white and background should be black.

img2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Draw the contoures
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)