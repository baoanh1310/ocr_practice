# Display some structuring elements in Morphological Transformation OpenCV
import cv2
import numpy as np

# Rectangular Kernel
morph_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
print("Morphology Rectangular:")
print(morph_rect)
print()

# Elliptical Kernel
morph_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print("Morphology Ellipse:")
print(morph_ellipse)
print()

# Cross-shaped Kernel
morph_cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
print("Morphology Cross-shaped:")
print(morph_cross)