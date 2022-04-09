from distutils.command.config import config
from logging import exception
from django.shortcuts import render
from distutils import extension
from sys import audit
from rest_framework import viewsets, parsers
from django.http import HttpResponse, response
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sklearn import exceptions
from .models import ImageData
from rest_framework import viewsets
from django.db.models import Q
from django.core import serializers
from rest_framework import status
from rest_framework.exceptions import NotFound 
from django.http import FileResponse 
from django.core.files.storage import FileSystemStorage
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files.base import ContentFile
import matplotlib.pyplot as plt
from .utils import get_filtered_image 
import base64
import json


from  .processing import horizontal_shift, sharpen ,vertical_shift,zoom,horizontal_flip,vertical_flip,rotation,horizontal_shift_mode
from .processing import blur ,sharpen

from .color_processing import brightness ,contrast ,to_gray ,to_hsv ,to_b,to_g,to_r
import pyrebase 

config ={
  "apiKey": "AIzaSyAa0h42SvEScIeJDC3T6QZlQh_bGR-jZkY",
  "authDomain": "augma-de550.firebaseapp.com",
  "projectId": "augma-de550",
  "databaseURL": "https://augma-de550-default-rtdb.firebaseio.com",
  "storageBucket": "augma-de550.appspot.com",
  "messagingSenderId": "619267377473",
  "appId": "1:619267377473:web:7a99d942fd70c8e68279c0",
  "measurementId": "G-XCXGKCN290"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
auth =firebase.auth() 

import random
def get_URL(img,name):
    im_pil = Image.fromarray(img)
    img = im_pil.resize((224,224), Image.ANTIALIAS)
    # myFile = "D:/Data-augmentation/augma/media/images/"+name+".jpeg"
    x= random.randint(2,10000) 
    
    try:
        myFile = "F:/MyProjects/augment/apps/augment-app/src/assets/images/"+name+ str(x)  + ".jpeg"
        img.save(myFile) 
    except:
        pass 
    saved_name = name+ str(x)  + ".jpeg"
    # storage.child("myFile"+name).put(myFile)
    # email="nrmethun@gmail.com"
    # password ="methun123" 
    # user =auth.sign_in_with_email_and_password(email,password)
    # url = storage.child("myFile"+name).get_url( user['idToken'] )
    # print(url)
    # print(">>>")
    return saved_name 

@api_view(['POST'])
def image_processing(request):
    try:

        # label= request.POST.get('types')
        print('check')
        types = json.loads(request.POST.get('types'))
        print(types)
        img = request.FILES["image"] 
        pil_img = Image.open(img)
        cv_img = np.array(pil_img)
        
        data =[]

        for item in types:
        ### vertical shift and ratio  

            if str(item['name']).strip() == 'vertical_shift':
                try:
                    val =float(item['value'][0]  ) /100 
                    vertical_shift_img = vertical_shift(cv_img , val ) 
                    v_shift_url=get_URL(vertical_shift_img,"v_shift_img") 
                    t= {   
                    "label": "Vertical Shift",
                    "url" : v_shift_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 
                except:
                    pass 

        ###  horizontal shift and ratio  
            elif str(item['name']).strip() == 'horizontal_shift' :
                try:
                    val =float(item['value'][0]) /100 
                    horizontal_shift_img = horizontal_shift(cv_img , val ) 
                    h_shift_url =get_URL(horizontal_shift_img,"h_shift_img") 

                    t= {          
                     "label": "Horizontal Shift",
                    "url" : h_shift_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 

        # ### Zooming
            elif str(item['name']).strip() == 'zoom' :
                try:
                    val =float(item['value'][0]) /100 
                    zoom_img = zoom(cv_img, val)
                    zoom_url = get_URL(zoom_img ,"zoom_img") 

                    t= {          
                      "label": "Zoom",
                    "url" : zoom_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 
            
            elif str(item['name']).strip() == 'horizontal_flip' :
                try:
                    # val =float(item['value']) /100 
                    ### horizontal Flip 
                    horizontal_flip_img = horizontal_flip(cv_img, True) 
                    h_flip_url = get_URL(horizontal_flip_img,"h_flip_img") 

                    t= {          
                      
                      "label": "Horizontal Flip",
                    "url" : h_flip_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 

            elif str(item['name']).strip() == 'vertical_flip' :
                try:
                    # val =float(item['value']) /100 
                    ### vertical Flip 
                    vertical_flip_img = vertical_flip(cv_img,True) 
                    v_flip_url = get_URL(vertical_flip_img,"h_flip_img") 

                    t= {          
                      
                      "label": "Vertical Flip",
                    "url" : v_flip_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 


            elif str(item['name']).strip()== 'rotation' :
                try:
                    # val =float(item['value']) /100 
                   ### Rotation
                    rotate_img = rotation(cv_img, int(item['value'][0]) ) 
                    rotate_url = get_URL(rotate_img,"rotate_img") 

                    t= {          
                      
                      "label": "Rotation",
                    "url" : rotate_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 

            
            elif str(item['name']).strip() == 'blur' :
                try:
                    # val =float(item['value']) /100 
                   ### Blur image 
                    blur_img = blur( cv_img , int(item['value'][0]) ) 
                    blur_url= get_URL(blur_img,"blur_img") 

                    t= {          
                      
                       "label": "Blur",
                    "url" : blur_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 

            elif str(item['name']).strip() == 'sharpen' :
                try:
                    # val =float(item['value']) /100 
                   ### Blur image 
                    sharp_img = sharpen( cv_img  ) 
                    sharp_url= get_URL(sharp_img,"sharp_img") 

                    t= {          
                      
                    "label": "Sharp",
                    "url" : sharp_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 
            
            elif str(item['name']).strip() == 'wrap' :
                try:
                    # val =float(item['value']) /100 
                   ### Blur image 
                    ### MODING ...wrap ,nearest , reflect , constant
                    special_mode_img = horizontal_shift_mode(cv_img, .5 ,'wrap')
                    wrap_url = get_URL(special_mode_img,"special_mode_img") 

                    t= {          
                     "label": "Image Wrap",
                    "url" : wrap_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 

            elif item['name'] == 'brightness' :
                try:
                    # val =float(item['value']) /100 
                   ### Brightness 
                    bright_img = brightness( cv_img ,180 ) 
                    bright_url= get_URL(bright_img,"bright_image")

                    t= {          
                     "label": "Image Wrap",
                    "url" : wrap_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 

            
            elif str(item['name']).strip()== 'contrast' :
                try:
                    # val =float(item['value']) /100 
                   ### contrast 
                    contrast_img = contrast( cv_img ,180 ) 
                    contrast_url= get_URL(contrast_img,"contrast_img") 

                    t= {          
                    "label": "contrast",
                    "url" : contrast_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 

            elif str(item['name']).strip() == 'to_hsv' :
                try:
                    # val =float(item['value']) /100 
                   ### to rgb to hsv 
                    hsv_img = to_hsv(cv_img) 
                    hsv_url = get_URL(hsv_img,"hsv_img")  

                    t= {          
                    "label": "HSV color-space",
                    "url" : hsv_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 
            
            elif str(item['name']).strip() == 'to_gray' :
                try:
                    # val =float(item['value']) /100 
                    ### to rgb to gray 
                    gray_img = to_gray(cv_img) 
                    gray_url = get_URL(gray_img ,'gray_img') 

                    t= {          
                    "label": "Gray image",
                    "url" : gray_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 

            elif str(item['name']).strip() == 'to_r' :
                try:
                    # val =float(item['value']) /100 
                    ### red channel 
                    red_img = to_r(cv_img) 
                    red_url = get_URL(red_img ,'red_img') 

                    t= {          
                    "label": "Red channel",
                    "url" : red_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 
            
            elif str(item['name']).strip() == 'to_g' :
                try:
                    # val =float(item['value']) /100 
                    ### green channel 
                    green_img = to_g(cv_img) 
                    green_url = get_URL(green_img ,'green_img') 

                    t= {          
                    "label": "Green  channel",
                    "url" : green_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 

            elif str(item['name']).strip()  == 'to_b' :
                try:
                    # val =float(item['value']) /100 
                    ### green channel 
                            ### blue channel 
                    blue_img = to_b(cv_img) 
                    blue_url = get_URL(blue_img ,'blue_img') 

                    t= {          
                    "label": "Blue  channel",
                    "url" : blue_url ,
                    "code" : "some code" 
                    } 
                    data.append(t) 

                except:
                    pass 
        

        print(data) 

        response={
            "status": 200 ,
            "message":"image Url data successfully found" ,
            "success":True,
            "data" : data 
            
        }
        return Response(response) 

    except  :
        response ={
                    "response_code" : 404,
                    "response_text" : 'failed to Image Urls',
                    "success" : False,
                    "error":[ {
                        "message": "failed to get Resources",
                        "code":404
                    }]
                }
        return Response(response) 


@api_view(['POST'])
def demo(request):
        print('check')
        # city_name = json.loads(request.POST.get('types'))
        # print(city_name)
        img = request.FILES["image"] 
        pil_img = Image.open(img)
        cv_img = np.array(pil_img) 
        blur_img = r( cv_img ,180 ) 

        plt.imshow(blur_img) 
        plt.show() 
        HttpResponse('done') 