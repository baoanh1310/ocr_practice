# Example of using Gradient Morphological Transformation using OpenCV
# USAGE
# python gradient.py --image j.png
import cv2
import argparse
import numpy as np 

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
	help="Path to the image")
args = vars(ap.parse_args())

# read image, create gradient, save output
img = cv2.imread(args["image"], 0)
kernel = np.ones((5, 5), np.uint8)

# Gradient is the difference between dilation and erosion of an image
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imwrite("j_gradient.png", gradient)