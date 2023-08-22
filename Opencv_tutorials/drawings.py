import cv2
'''
This file involves drawing a line, circle, rectangle and putting a text
on the picture 
'''


img = cv2.imread('Images/OIP.jpg')
img = cv2.line(img, (400,400), (50,25),(0,0,255), 3)
img = cv2.circle(img, (200,200),50,(255,0,0),4)
img = cv2.rectangle(img, (300,300), (100,100), (0,255,0),3)
# putting a text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'This is my pic', (100,330), font, 1, (0,0,0),3)
cv2.imshow('image',img)
cv2.waitKey(0)

cv2.destroyAllWindows()