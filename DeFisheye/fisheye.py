from defisheye import Defisheye
import cv2
import os

def fisheye_image(input_img, output_img, dtype='linear', format='fullframe', fov=220, pfov=120):
    
    output_dir = os.path.dirname(output_img)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # setting defisheye object
    obj = Defisheye(input_img, dtype=dtype, format=format, fov=fov, pfov=pfov)

    # convert fisheye image and save the output
    obj.convert(outfile=output_img)

input_img = "C:/Users/ibroh/Downloads/fisheye.jpg"
output_img = "C:/Users/ibroh/OneDrive/Desktop/defisheye/resultFishEye.jpg"

fisheye_image(input_img, output_img)

# Read the saved output image
output_img = cv2.imread(output_img)

# Display 
cv2.imshow('Converted Image', output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()













