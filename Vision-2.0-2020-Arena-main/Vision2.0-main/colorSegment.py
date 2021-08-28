import cv2
import numpy as np

class img_process:
    val = np.zeros([9, 9], dtype="uint8")
    mid = np.zeros([9, 9, 2], dtype="uint16")
    k = np.zeros(81, dtype="uint8")
    x=0
    y=0
    f=0

    def __init__(self,img):
        self.img=img
        self.find_dim()
        self.process_red()
        self.process_yellow()

        print(self.val)
        c = 0
        for i in range(0, 9):
            for j in range(0, 9):
                self.k[c] = self.val[j, i]
                c = c + 1
        self.mid[4,0]=[self.mid[3,0,0],self.mid[4,1,1]]
        self.mid[0,4]=[self.mid[1,4,0],self.mid[0,3,1]]
        self.mid[8,4]=[self.mid[7,4,0],self.mid[8,3,1]]
        self.mid[4,8]=[self.mid[3,8,0],self.mid[4,7,1]]
        self.mid[4,4]=[self.mid[3,4,0],self.mid[4,3,1]]

    def bot_pos(self,a,b):
        for i in range(0,9):
            for j in range(0,9):
                if(self.x+i*self.f<=a<=self.x+(i+1)*self.f)&(self.y+j*self.f<=b<=self.y+(j+1)*self.f):
                    return (i*9+j)

    def assign(self,cnt,l):

        M = cv2.moments(cnt)
        a,b = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        #cv2.drawContours(img2, [approx], -1, (0, 255, 0), 1)
        if cv2.contourArea(cnt)>250:
            if len(approx) == 3:
                m=1
            elif len(approx) == 4:
                m=2
            else:
                m=3
        for i in range(0,9):
            for j in range(0,9):
                if(self.x+i*self.f<=a<=self.x+(i+1)*self.f)&(self.y+j*self.f<=b<=self.y+(j+1)*self.f)&(cv2.contourArea(cnt)>250):
                    self.val[j,i]=l+m
                    #self.mid[j,i,0]=self.x+i*self.f +self.f/2
                    #self.mid[j,i,1]=self.y+j*self.f +self.f/2
                    self.mid[j,i,0]=a
                    self.mid[j,i,1]=b
                



    def find_dim(self):
        img=self.img
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([180, 5, 5])

        mask = cv2.inRange(hsv, lower_black, upper_black)

        cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cntsSorted = sorted(cnts, key=lambda x: cv2.contourArea(x))
        
        xm=1000
        ym=1000
        wm=1000
        hm=1000
        for i in (3,4,5,6):
            x, y, w, h = cv2.boundingRect(cntsSorted[len(cntsSorted) - i])
            #print(x,y,w,h)
            xm=min(xm,x)
            ym=min(ym,y)
            wm=min(wm,w)
            hm=min(hm,h)

        self.f = min(wm, hm) / 3
        self.x=xm-self.f
        self.y=ym-self.f

    def process_yellow(self):
        img = self.img
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([25, 100, 150])
        upper_yellow = np.array([40, 255, 255])
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        #cv2.imshow('yellow mask', mask)

        cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in cnts:
            img_process.assign(self,cnt,0)


    def process_red(self):
        img = self.img
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_red1 = np.array([0, 100, 50])
        upper_red1 = np.array([20, 255, 255])

        lower_red2 = np.array([170, 100, 50])
        upper_red2 = np.array([180, 255, 255])

        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask1 = mask1 + mask2
        #cv2.imshow('red mask', mask1)

        cnts, _ = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in cnts:
            img_process.assign(self,cnt,3)


    def get_val(self):

        #cv2.imshow('image', self.img)

        #cv2.waitKey(0);

        return self.k;


