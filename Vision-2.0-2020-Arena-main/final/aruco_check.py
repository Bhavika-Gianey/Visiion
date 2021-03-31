import numpy as np
import cv2
import math
import cv2.aruco as aruco

aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_250)
img = aruco.drawMarker(aruco_dict , 20 , 400)
cv2.imshow('aruco20',img)
cv2.waitKey(0)
##img = cv2.imread('C:/Users/hp/Pictures/Screenshots/Screenshot (84).png')
##img = cv2.resize(img,(1280,720))
##cv2.imshow('sample',img)
##cv2.waitKey(0)
##gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##parameters = aruco.DetectorParameters_create()
##corners , ids , _ = aruco.detectMarkers(gray , aruco_dict,parameters = parameters)
##print(corners)
##print((corners[0][0][0][0]+corners[0][0][1][0])/2)
##
##print(ids)
cv2.destroyAllWindows()
