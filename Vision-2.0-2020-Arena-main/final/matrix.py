import gym
import vision_arena
import time
import pybullet as p
import pybullet_data
import cv2
import numpy as np
import os


def Thresh(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
##    cv2.imshow('hsv',hsv)
    threshY = cv2.inRange(hsv, Y[0], Y[1])
    threshR = cv2.inRange(hsv, R[0], R[1])
    thresh = cv2.bitwise_or(threshR, threshY)
##    cv2.imshow('threshY',threshY)
##    cv2.imshow('threshR',threshR)
##    cv2.imshow('thresh',thresh)
    imgY = cv2.bitwise_and(frame, frame, mask=threshY)
    imgR = cv2.bitwise_and(frame, frame, mask=threshR)
    img = cv2.bitwise_and(frame, frame, mask=thresh)
    cv2.imshow('imgY',imgY)
    cv2.imshow('imgR',imgR)
    cv2.imshow('img',img)

    contoursR,hR = cv2.findContours(threshR,1,2)
    contoursY,hY = cv2.findContours(threshY,1,2)
    contours,h = cv2.findContours(thresh,1,2)

    shapeDetection(contoursR,'Red')
    shapeDetection(contoursY,'Yellow')




def shapeDetection(contours,color):
    for cnt in contours:
        epsilon = 0.02*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        M = cv2.moments(cnt)
        x,y,w,h = cv2.boundingRect(cnt)
        cx=int(M["m10"]/M["m00"])
        cy=int(M["m01"]/M["m00"])
        p=cy//50
        q=cx//50
        centroidX[p][q]=cx
        centroidY[p][q]=cy
##        print (len(approx))
        if len(approx)==3:
##             print (len(approx))
             print (color," triangle")
             if(color=='Red'):
                 b[p][q]=1
             else:
                 b[p][q]=4

        elif len(approx)==4:
##             print (len(approx))
             print (color, " square")
             if(color=='Red'):
                 b[p][q]=2
             else:
                 b[p][q]=5
        elif len(approx)>4 and len(approx)<10:
##             print (len(approx))
             print (color, " circle")
             if(color=='Red'):
                 b[p][q]=3
             else:
                 b[p][q]=6


if __name__=="__main__":
    parent_path = os.path.dirname(os.getcwd())
    os.chdir(parent_path)
    env = gym.make("vision_arena-v0")
    time.sleep(3)
    env.remove_car()
    time.sleep(3)
    frame = env.camera_feed()
    roi = cv2.selectROI(frame)
    frame = frame[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
    frame=cv2.resize(frame,(450,450))
    cv2.imshow('frame',frame)
    b=np.zeros((9,9))
    #  SIGN CONVENTION
    # 1- Red triangle
    # 2- Red SQuare
    # 3- Red circle
    # 4- Yellow triangle
    # 5- Yellow square
    # 6- Yellow circle
    # 7- Black arrow
    # 8- Home
    b[0][4] = b[4][0] = b[8][4] = b[4][8] =7
    b[4][4] = 8
    ##cv2.waitKey(0)
    ##cv2.destroyAllWindows()
    ##height, width = frame.shape[:2]
    ##print(height)
    ##print(width)
    centroidX=np.zeros((9,9))
    centroidY=np.zeros((9,9))
    Y=np.array([ [20, 100, 130], [35, 255, 255] ])
    R=np.array([ [0, 125, 125], [10, 255, 200] ])


    Thresh(frame)
    print(b)
    centroidX[0][4]=centroidX[4][4]=centroidX[8][4]=centroidX[1][4]
    centroidX[4][0]=centroidX[3][0]
    centroidX[4][8]=centroidX[3][8]
    centroidY[0][4]=centroidY[0][0]
    centroidY[4][4]=centroidY[4][0]=centroidY[4][8]=centroidY[4][1]
    centroidY[8][4]=centroidY[8][0]
    print(centroidX)
    print(centroidY)

    np.save('shape.npy', b)
    np.save('centroidX.npy', centroidX)
    np.save('centroidY.npy', centroidY)
    env.respawn_car()
    # time.sleep(3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # time.sleep(100)
