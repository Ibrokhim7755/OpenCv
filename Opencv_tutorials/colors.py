import cv2
import numpy as np



cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Define the lower and upper bounds for red color in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
        
    # Lower and upper bounds for detecting yellow color in HSV
    lower_yellow = np.array([20, 100, 100])   
    upper_yellow = np.array([40, 255, 255]) 
    
        
    # Lower and upper bounds for detecting green color in HSV
    lower_green = np.array([40, 40, 40])   
    upper_green = np.array([80, 255, 255])   
    
    red = cv2.inRange(img,lower_red, upper_red)
    yellow = cv2.inRange(img,lower_yellow, upper_yellow)
    green = cv2.inRange(img,lower_green, upper_green)
    
    mask = red + yellow + green
    
    out = cv2.bitwise_and(img,img, mask=mask)
    
    cv2.imshow('Original', frame)
    cv2.imshow('frame', out)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()