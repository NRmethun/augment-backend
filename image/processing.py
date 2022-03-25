
import cv2
from PIL import Image 
import numpy as np 
import random

def fill(img, h, w):
    img = cv2.resize(img, (h, w), cv2.INTER_CUBIC)
    return img

#  shifting        
def horizontal_shift(img, ratio=0.0):
    if ratio > 1 or ratio < 0:
        print('Value should be less than 1 and greater than 0')
        return img
    ratio = random.uniform(-ratio, ratio)
    h, w = img.shape[:2]
    to_shift = w*ratio
    if ratio > 0:
        img = img[:, :int(w-to_shift), :]
    if ratio < 0:
        img = img[:, int(-1*to_shift):, :]
    img = fill(img, h, w) 
    return img 

def vertical_shift(img, ratio=0.0):
    if ratio > 1 or ratio < 0:
        print('Value should be less than 1 and greater than 0')
        return img
    ratio = random.uniform(-ratio, ratio)
    h, w = img.shape[:2]
    to_shift = h*ratio
    if ratio > 0:
        img = img[:int(h-to_shift), :, :]
    if ratio < 0:
        img = img[int(-1*to_shift):, :, :]
    img = fill(img, h, w)
    return img

#  Zooming 
def zoom(img, value):
    if value > 1 or value < 0:
        print('Value for zoom should be less than 1 and greater than 0')
        return img
    value = random.uniform(value, 1)
    h, w = img.shape[:2]
    h_taken = int(value*h)
    w_taken = int(value*w)
    h_start = random.randint(0, h-h_taken)
    w_start = random.randint(0, w-w_taken)
    img = img[h_start:h_start+h_taken, w_start:w_start+w_taken, :]
    img = fill(img, h, w)
    return img
# Fliping 
def horizontal_flip(img, flag):
    if flag:
        return cv2.flip(img, 1)
    else:
        return img 

def vertical_flip(img, flag):
    if flag:
        return cv2.flip(img, 0)
    else:
        return img 

# Rotation 
def rotation(img, angle):
    angle = int(random.uniform(-angle, angle))
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), angle, 1)
    img = cv2.warpAffine(img, M, (w, h))
    return img

#  moDEING 
def nearest_mode(img, left, right):
    nearest = cv2.copyMakeBorder(img, 0, 0, left, right, cv2.BORDER_REPLICATE)
    return nearest 
def reflect_mode(img, left, right):
    reflect = cv2.copyMakeBorder(img, 0, 0, left, right, cv2.BORDER_REFLECT)
    return reflect
def wrap_mode(img, left, right) :
    wrap = cv2.copyMakeBorder(img, 0, 0, left, right, cv2.BORDER_WRAP)
    return wrap
def constant_mode(img, left, right):
    constant= cv2.copyMakeBorder(img, 0, 0, left, right, cv2.BORDER_CONSTANT,value=(255, 0, 0))
    return constant

def horizontal_shift_mode(img, ratio , type):
    if ratio > 1 or ratio < 0:
        print('Value for horizontal shift should be less than 1 and greater than 0')
        return img
    ratio = random.uniform(-ratio, ratio)
    h, w = img.shape[:2]
    to_shift = int(w*ratio)
    fill =img 
    if ratio > 0:
        img = img[:, :w-to_shift, :]
        if(type=='nearest') :
            fill =nearest_mode(img, to_shift, 0) 
        elif(type=='reflect'):
            fill = reflect_mode(img, to_shift, 0) 
        elif (type == 'wrap') :
            fill = wrap_mode(img, to_shift, 0) 
        else :
            fill = constant_mode(img, to_shift, 0)
    if ratio < 0:
        img = img[:, -1*to_shift:, :] 
        if(type=='nearest') :
            fill =nearest_mode(img, 0, -1*to_shift)
        elif(type=='reflect'):
            fill = reflect_mode(img, 0, -1*to_shift)
        elif (type == 'wrap') :
            fill = wrap_mode(img, 0, -1*to_shift)
        else :
            fill = constant_mode(img, 0, -1*to_shift)
    return fill

#### //////////////////////// 


