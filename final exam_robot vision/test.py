import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm
from PIL import Image
import requests

img=cv2.imread("Resources/secret_message.png")
dimg=cv2.imread("Resources/down.png")

img=cv2.resize(img,(640,480))
dimg=cv2.resize(dimg,(640,480))

a=200
text=(dimg-((1-a)*img))/a
cv2.imshow("a",text)
cv2.waitKey(0)