import cv2
from PIL import Image 
import numpy as np 

def get_filtered_image(image, action):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    filtered = None
    if action == 'NO_FILTER':
        filtered = image
    elif action == 'COLORIZED':
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif action == 'GRAYSCALE':
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif action == 'BLURRED':
        width, height = img.shape[:2]
        if width > 500:
            k = (50, 50)
        elif width > 200 and width <=500:
            k = (25,25)
        else:
            k = (10,10)
        blur = cv2.blur(img, k)
        filtered = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)
    elif action == 'BINARY':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, filtered = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    elif action == 'INVERT':
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        filtered = cv2.bitwise_not(img)
    elif action == 'flip' :
        # vertical 
        filtered = cv2.flip(image, 0) 
    elif action == 'rotate' :
        filtered = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
        # image = cv2.rotate(src, cv2.ROTATE_180)
        # cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
    elif action == 'crop' :
        print('kkk')
        # height, width, _ = image.shape
        # left = 6
        # print('kkk ', height)
        # top = height / 4
        # right = 174
        # bottom = 3 * height / 4
        # im1 = image.crop((left, top, right, bottom))
        # print('kkk')
        # newsize = (200, 200)
        # print('kkk')

        hgt, wdt = image.shape[:2]
        print(hgt , wdt) 
        start_row, start_col = int(hgt * .25), int(wdt * .25)
        print(start_row,start_col) 
        end_row, end_col = int(hgt * .75), int(wdt * .75)
        print(end_row,end_col)
        filtered = image[start_row:end_row , start_col:end_col]
        # plt.subplot(2, 2, 2)
        # plt.imshow(cropped)
        # filtered = im1.transpose(Image.FLIP_LEFT_RIGHT)
        print('kkk')
    elif action=='sharpening' :
        print('sharp')
        kernel_sharpening = np.array([[-1,-1,-1], 
                              [-1,9,-1], 
                              [-1,-1,-1]])
        sharpened = cv2.filter2D(image, -1, kernel_sharpening)
        filtered =sharpened 
    elif action == 'bluring' :
        # kernel_7x7 = np.ones((7, 7), np.float32) / 49
        # blurred2 = cv2.filter2D(image, -1, kernel_7x7)
        kernel_3x3 = np.ones((3, 3), np.float32) / 9
        blurred = cv2.filter2D(image, -1, kernel_3x3)
        filtered = blurred

    return filtered