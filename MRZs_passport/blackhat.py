# Example of using Blackhat Morphological Transformation using OpenCV
# USAGE
# python blackhat.py --image mrz_original.jpg
import cv2
import argparse
import numpy as np 

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
	help="Path to the image")
args = vars(ap.parse_args())

# read image, blackhat, save output
img = cv2.imread(args["image"], 0)
kernel = np.ones((5, 5), np.uint8)

# Black Hat is the difference between the closing of the input image and input image
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imwrite("mrz_blackhat.png", blackhat)