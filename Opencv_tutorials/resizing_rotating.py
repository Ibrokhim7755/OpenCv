import cv2
import numpy as np

# Read the image using imread() function

image = cv2.imread('Images/detection.jpg')
cv2.imshow('Original Image', image)
 

# Lets downscale the image using a new widths and heights
down_w = 300
down_h = 200
downpoint = (down_w, down_h)
resized_down = cv2.resize(image, downpoint, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resized Downscale image', resized_down)

# Lets upscale the image using a new widths and heights
up_width = 600
up_height = 400
up_point = (up_width, up_height)
resized_up = cv2.resize(image, up_point, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Resized Upscale image', resized_down)

rotate = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated', rotate)

cv2.waitKey(0)
#press any key to quit the code
cv2.destroyAllWindows()