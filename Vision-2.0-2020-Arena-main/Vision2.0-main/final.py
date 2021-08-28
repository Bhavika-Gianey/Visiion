import colorSegment as color_segment
import BFS as bfs
import AdjMat
import cv2
import numpy as np
import gym
import vision_arena
import time
import pybullet as p
import pybullet_data
import Aruco as aruco_test
import math

def get_aruco(dest):
    get = env.camera_feed()
    dis,ang,cen = aruco_test.GetAruco(get,dest).detectAruco()
    while(dis==0 and ang==0 and cen==0):
            right(0)
            get = env.camera_feed()
            dis,ang,cen = aruco_test.GetAruco(get,dest).detectAruco()
    return dis,ang,cen

def right(ang):
    if ang==0:
        k=20
    else:
        k=max(math.ceil(ang*3),50)
    c=2
    for i in range(0,k):
        p.stepSimulation()
        env.move_husky(c, -1*c, c, -1*c)

def left(ang):
    k=max(math.ceil(ang*3),50)
    c=2
    for i in range(0,k):
        p.stepSimulation()
        env.move_husky(-1*c, c, -1*c, c)

def move(dis):
    k=max(math.ceil(3*dis),40)
    c=4
    for i in range(0,k):
        p.stepSimulation()
        env.move_husky(c, c, c, c)

def stop():
    p.stepSimulation()
    env.move_husky(0, 0, 0, 0)

def align(dest):
    p=0
    dis,ang,cnrs = get_aruco(dest)
    while abs(ang)>5:
        dis,ang,cnrs = get_aruco(dest)
        if(ang>2.0):
            right(abs(ang))
        if(ang<-2.0):
            left(abs(ang))
        stop()

def travel(dest):
    dis,ang,cnrs = get_aruco(dest)
    disprev=dis
    
    while dis>5:
        dis,ang,cnrs = get_aruco(dest)
        if(dis>disprev):
            break
        move(dis)
        disprev=dis
        stop()


if __name__=="__main__":
    env = gym.make("vision_arena-v0")
    
    img = env.camera_feed()
    A = color_segment.img_process(img)
    val = A.get_val()
    mid = A.mid

    get = env.camera_feed()
    dis,ang,cen = aruco_test.GetAruco(get,(0,0)).detectAruco()
    cv2.imshow('get',get)
    cv2.waitKey(0)
    cur= A.bot_pos(cen[0],cen[1])
    print("starting from:",cur)

    B = AdjMat.adj_mat(cur)

    while True:
        s = env.roll_dice()
        C = bfs.FindPath(B.adj, val, cur, s)
        print("Destination:",s)
        print("path")
        print(C.path)
        for i in C.path:
            print("********")
            print("cur:",cur)
            print("dest:",i)
            align(tuple(mid[i%9,i//9]))
            travel(tuple(mid[i%9,i//9]))
            B.adj_update(a=cur, b=i)
            #B.show()
            cur = i
        
        for i in range(0,81):
            C.parent[i]=-1
        C.end = -1
        C.path = []
        if cur==40:
            break

    time.sleep(100)
