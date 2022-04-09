
import cv2

import numpy as np 
import random
from PIL import Image, ImageEnhance 


def fill(img, h, w):
    img = cv2.resize(img, (h, w), cv2.INTER_CUBIC)
    return img
def brightness(img, brightness):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            max = 255
        else:
            shadow = 0
            max = 255 + brightness
    al_pha = (max - shadow) / 255
    ga_mma = shadow
    img = cv2.addWeighted(img, al_pha, img, 0, ga_mma) 
    h, w = img.shape[:2] 
    img = fill(img, h, w) 
    return img 
    

def contrast(img ,contrast) :

    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127)) 
    Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
    Gamma = 127 * (1 - Alpha)
    img = cv2.addWeighted(img, Alpha,img, 0, Gamma)
    h, w = img.shape[:2] 
    img = fill(img, h, w) 
    return img 

    
def to_gray(img) :
    ii = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
    h, w = ii.shape[:2] 
    img = fill(ii, h, w) 

    return img 

def to_hsv(img) :
    ii = cv2.cvtColor(img, cv2.COLOR_RGB2HSV) 
    h, w = ii.shape[:2] 
    img = fill(ii, h, w) 

    return img 

def to_r(img):
    (R, G, B) = cv2.split(img) 
    h, w = R.shape[:2] 
    img = fill(R, h, w)
    return img  
def to_g(img):
    (R, G, B) = cv2.split(img) 
    h, w = G.shape[:2] 
    img = fill(G, h, w)
    return img 
def to_b(img):
    (R, G, B) = cv2.split(img) 
    h, w = B.shape[:2] 
    img = fill(B, h, w)
    return img 

