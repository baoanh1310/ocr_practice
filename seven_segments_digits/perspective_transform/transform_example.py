# USAGE
# python transform_example.py --image img.png --coords "[(73, 239), (356, 117), (475, 265), (187, 443)]"

from transform import four_point_transform
import numpy as np 
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image")
ap.add_argument("-c", "--coords",
	help="comma separated list of source points")
args = vars(ap.parse_args())

# load the image and grab the source coordinates (i.e. the list of
# of (x, y) points)
# NOTE: using the 'eval' function is bad form, but for this example
# let's just roll with it -- in future posts I'll show you how to
# automatically determine the coordinates without pre-supplying them
image = cv2.imread(args["image"])
pts = np.array(eval(args["coords"]), dtype = "float32")
# apply the four point tranform to obtain a "birds eye view" of
# the image
warped = four_point_transform(image, pts)
# show the original and warped images
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)