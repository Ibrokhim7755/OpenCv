import cv2

'''
OpenCV, the largest computer vision library in the world has these three built-in functions,
let’s find out what exactly each one does:

1) imread() helps us read an image.
2) imshow() displays an image in a window.
'''

# Read an image

im_color = cv2.imread('Images/Blue_Bugatti_Car_HD_Image.jpg', cv2.IMREAD_COLOR)
im_gray = cv2.imread('Images/Blue_Bugatti_Car_HD_Image.jpg', cv2.IMREAD_GRAYSCALE)
im_unchanged = cv2.imread('Images/Blue_Bugatti_Car_HD_Image.jpg', cv2.IMREAD_UNCHANGED)

#print(im_color.shape)
cv2.imshow('color',im_color)
cv2.imshow('gray',im_gray)
cv2.imshow('unchanged',im_unchanged)

cv2.waitKey(0)
cv2.destroyAllWindows()