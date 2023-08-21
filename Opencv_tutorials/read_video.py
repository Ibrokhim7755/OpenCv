import cv2
import numpy as np

'''
Reading and writing videos in OpenCV is very similar to reading and writing images. 
A video is nothing but a series of images that are often referred to as frames. 
So, all we need to do is loop over all the frames in a video sequence,
and then process one frame at a time. In this file, i will demonstrate how to read, 
display and write videos from a file, an image sequence and a webcam.
'''


cap = cv2.VideoCapture('Videos/bottle-detection.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            

    
'''
Now what i am gonna do is, i will devide the camera into four parts and try
read and show what is gonna happen.
'''

vid = cv2.VideoCapture(0)

while True:
    succes, frem = vid.read()
    width = int(vid.get(3))
    height = int(vid.get(4))
    
    img = np.zeros(frem.shape, np.uint8)
    small_frem = cv2.resize(frem, (0,0), fx=0.5, fy=0.5) # resizing cameras into half 
    
    img[:height//2, :width//2] = small_frem
    img[height//2:, :width//2] = small_frem
    img[:height//2, width//2:] = small_frem
    img[height//2:, width//2:] = small_frem
    
    cv2.imshow('frem', img)

    if cv2.waitKey(1) == ord('q'):
        break
    
vid.release()
cv2.destroyAllWindows()