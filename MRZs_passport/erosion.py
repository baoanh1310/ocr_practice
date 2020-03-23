# Example of using Erosion Morphological Transformation using OpenCV
# USAGE
# python erosion --image j.png
import cv2
import argparse
import numpy as np 

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
	help="Path to the image")
args = vars(ap.parse_args())

# read image, erode, save output
img = cv2.imread(args["image"], 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

cv2.imwrite("j_erosion.png", erosion)