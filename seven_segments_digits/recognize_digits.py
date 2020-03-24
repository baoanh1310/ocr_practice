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
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)

cv2.imwrite("step1_result.png", edged)