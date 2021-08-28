import cv2
import numpy as np

class adj_mat:
    adj = np.zeros([82, 82], dtype="uint8")
    home = 0
    
    def __init__(self,home):
        self.adj_init()
        self.home= home
        
    def adj_init(self):
    
        #FOR OUTER SQUARE
        for i in range(0, 64, 9):
            self.adj[i, i + 9] = 1
    
        for i in range(72, 80):
            self.adj[i, i + 1] = 1
    
        for i in range(8, 72, 9):
            self.adj[i + 9, i] = 1
    
        for i in range(0, 8):
            self.adj[i + 1, i] = 1
    
        #FOR INNER SQUARE
        for i in range(20, 48, 9):
            self.adj[i, i + 9] = 1
    
        for i in range(56, 60):
            self.adj[i, i + 1] = 1
    
        for i in range(24, 52, 9):
            self.adj[i + 9, i] = 1
    
        for i in range(20, 24):
            self.adj[i + 1, i] = 1
    
        #FOR LINKS BETWEEN THE SQUARE
        for i in range(4,14,9):
            self.adj[i,i+9] = 1
            self.adj[i+9,i] = 1
    
        for i in range(58,68,9):
            self.adj[i,i+9] = 1
            self.adj[i+9,i] = 1
    
        for i in range(36,38):
            self.adj[i,i+1] = 1
            self.adj[i+1,i] = 1
    
        for i in range(42,44):
            self.adj[i,i+1] = 1
            self.adj[i+1,i] = 1
    
    def adj_update(self, a, b):
    
        self.adj[a,b] = 0
    
        #condition to restore the edge between points if the travel was between the squares
        if (a in (4,13,58,67)) & (b==a+9):
            self.adj[a,b]=1
        if (a in (13,22,67,76)) & (b==a-9):
            self.adj[a,b]=1
        if (a in (36,37,42,43)) & (b==a+1):
            self.adj[a,b]=1
        if (a in (37,38,43,44)) & (b==a-1):
            self.adj[a,b]=1
    
    
        #traversed in outer so can't traverse the corresponding in inner
        if(a==4)&(b==3):
            for i in range(20, 22):
                self.adj[i + 1, i] = 0
            for i in range(20, 30, 9):
                self.adj[i, i + 9] = 0
    
            for i in (4,13):
                self.adj[i, i + 9] = 0
                self.adj[i + 9, i] = 0
    
    
        if(a==36)&(b==45):
            for i in range(38, 48, 9):
                self.adj[i, i + 9] = 0
            for i in range(56, 58):
                self.adj[i, i + 1] = 0
    
            for i in (36,37):
                self.adj[i, i + 1] = 0
                self.adj[i + 1, i] = 0
    
        if(a==76)&(b==77):
            for i in range(58, 60):
                self.adj[i, i + 1] = 0
            for i in range(42, 52, 9):
                self.adj[i + 9, i] = 0
    
            for i in (58,67):
                self.adj[i, i + 9] = 0
                self.adj[i + 9, i] = 0
    
        if(a==44)&(b==35):
            for i in range(24, 34, 9):
                self.adj[i + 9, i] = 0
            for i in range(22, 24):
                self.adj[i + 1, i] = 0
    
            for i in (42,43):
                self.adj[i, i + 1] = 0
                self.adj[i + 1, i] = 0
    
        # traversed in inner so can't traverse the corresponding part in outer
        if(a==22)&(b==21):
            for i in (0,1,2,3):
                self.adj[i+1,i] = 0
            for i in (0, 9, 18, 27):
                self.adj[i,i+9] = 0
    
            for i in (4,13):
                self.adj[i, i + 9] = 0
                self.adj[i + 9, i] = 0
    
        if(a==38)&(b==47):
            for i in (36, 45, 54, 63):
                self.adj[i,i+9] = 0
            for i in (72, 73, 74, 75):
                self.adj[i,i+1] = 0
    
            for i in (36,37):
                self.adj[i, i + 1] = 0
                self.adj[i + 1, i] = 0
    
        if(a==58)&(b==59):
            for i in (76, 77, 78, 79):
                self.adj[i,i+1] = 0
            for i in (44, 53, 62, 71):
                self.adj[i+9,i] = 0
    
            for i in (58,67):
                self.adj[i, i + 9] = 0
                self.adj[i + 9, i] = 0
    
        if(a==42)&(b==33):
            for i in (4,5,6,7):
                self.adj[i+1,i] = 0
            for i in (8,17,26,35):
                self.adj[i+9,i] = 0
    
            for i in (42,43):
                self.adj[i, i + 1] = 0
                self.adj[i + 1, i] = 0

        if(self.home==4):
            if (a==4 and b==3) or (a==22 and b==21):
                for i in (4,13,22):
                    self.adj[i, i+9]=1
                    self.adj[i+9, i]=1

        if(self.home==36):
            if (a==36 and b==45) or (a==38 and b==47):
                for i in (36,37,38):
                    self.adj[i, i+1]=1
                    self.adj[i+1, i]=1

        if(self.home==76):
            if (a==76 and b==77) or (a==58 and b==59):
                for i in (49,58,67):
                    self.adj[i, i+9]=1
                    self.adj[i+9, i]=1

        if(self.home==44):
            if (a==44 and b==35) or (a==42 and b==33):
                for i in (41,42,43):
                    self.adj[i, i+1]=1
                    self.adj[i+1, i]=1
    
    def show(self):
        img = np.ones((450, 450, 3), dtype="uint8") * 255

        c = 0
        for i in range(0, 9):
            for j in range(0, 9):
                cv2.circle(img, (i * 50 + 25, j * 50 + 25), 3, (0))
                if (c <= 71):
                    if (self.adj[c, c + 9] == 1):
                        cv2.line(img, (i * 50 + 25, j * 50 + 25), (i * 50 + 50, j * 50 + 25), color=(0), thickness=1)
                if (c <= 79):
                    if (self.adj[c, c + 1] == 1):
                        cv2.line(img, (i * 50 + 25, j * 50 + 25), (i * 50 + 25, j * 50 + 50), color=(0), thickness=1)
                if (c >= 9):
                    if (self.adj[c, c - 9] == 1):
                        cv2.line(img, (i * 50 + 25, j * 50 + 25), (i * 50, j * 50 + 25), color=(0), thickness=1)
                if (c >= 1):
                    if (self.adj[c, c - 1] == 1):
                        cv2.line(img, (i * 50 + 25, j * 50 + 25), (i * 50 + 25, j * 50), color=(0), thickness=1)
                c = c + 1

        cv2.imshow('image', img)
        cv2.waitKey(0)



#self.adj_update(3,2)


#print((self.adj[73,74]))
# cv2.putText(img, str(j), (i*50 +25,j*50 + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0), None)