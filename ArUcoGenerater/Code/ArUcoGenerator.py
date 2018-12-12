# -*- coding: utf-8 -*-
"""
ArUco ID Dictionaries: 4X4 = 4-bit pixel, 4X4_50 = 50 combinations of a 4-bit pixel image
List of Dictionaries in OpenCV's ArUco library:
DICT_4X4_50	 
DICT_4X4_100	 
DICT_4X4_250	 
DICT_4X4_1000	 
DICT_5X5_50	 
DICT_5X5_100	 
DICT_5X5_250	 
DICT_5X5_1000	 
DICT_6X6_50	 
DICT_6X6_100	 
DICT_6X6_250	 
DICT_6X6_1000	 
DICT_7X7_50	 
DICT_7X7_100	 
DICT_7X7_250	 
DICT_7X7_1000	 
DICT_ARUCO_ORIGINAL

Reference: http://hackage.haskell.org/package/opencv-extra-0.2.0.1/docs/OpenCV-Extra-ArUco.html
"""

import numpy
import cv2
import cv2.aruco as aruco

def aruco_gen(id_aruco, num_pixels):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)     # aruco.DICT_nXn_C , replace n with no. of bits per pixel and C with the no. of combinations
    WHITE =[255,255,255]                                                        #select n and C from the list mentioned above
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = aruco.drawMarker(aruco_dict, id_aruco, num_pixels)
    constant= cv2.copyMakeBorder(img,25,25,25,25,cv2.BORDER_CONSTANT,value=WHITE)
    i=cv2.putText(constant,'ArUco ID = '+ str(id_aruco), (155, 15), font, 0.5,(0,0,255), 2 , )
    cv2.imshow('ArUco',i)
    cv2.imwrite('ArUco'+str(id_aruco)+'.jpg',i)
    cv2.waitKey(0)

    '''
    code here for saving the Aruco image as a "jpg" by following the steps below:
    1. save the image as a colour RGB image in OpenCV color image format
    2. embed a boundary of 25 pixels on all four sides and three channels of the image
    3. save the image as "ArUcoID.jpg" where ID is the digits of id_aruco i.e. if the ID is 26 the name should be: ArUco26.jpg
    4. You are permitted to modify n, C and variables id_aruco and num_pixels
    '''

    cv2.destroyAllWindows()


if __name__ == "__main__":    
    aruco_gen(199, 400) #write id_aruco whos id you want to see also write num_pixels i.e pixels of a display image
                           
    
