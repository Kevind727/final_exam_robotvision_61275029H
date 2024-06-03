
import numpy as np
import random
import math

def generator(size, _theta=10.0/180.0*math.pi):
    img = np.zeros(size, dtype=np.uint8)
    n = random.randint(5,15)
    
    for k in range(n):
        l = random.randint(size[0]//2,size[0])
        d = 0
        x,y = random.randint(0, size[0]-1),random.randint(0, size[1]-1)
        theta = _theta
        while(d < l):
            if (random.random() < 0.2):
                theta = random.gauss(_theta,math.pi/5)
            x,y = x + math.cos(theta), y-math.sin(theta)
            if (x>=0)and(x<len(img[0]))and(y>=0)and(y<len(img)):
                img[int(y),int(x)] = 255
            d = d + 1
    return img
