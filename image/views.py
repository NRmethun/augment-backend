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


from  .processing import horizontal_shift ,vertical_shift,zoom,horizontal_flip,vertical_flip,rotation,horizontal_shift_mode
from .color_processing import brightness
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

def get_URL(img,name):
    im_pil = Image.fromarray(img)
    img = im_pil.resize((224,224), Image.ANTIALIAS)
    myFile = "D:/Data-augmentation/augma/media/images/"+name+".jpeg"
    img.save(myFile)
    storage.child("myFile").put(myFile)
    email="nrmethun@gmail.com"
    password ="methun123" 
    user =auth.sign_in_with_email_and_password(email,password)
    url = storage.child('filename.jpeg').get_url( user['idToken'] )
    return url 

@api_view(['POST'])
def image_processing(request):
    try:

        label= request.POST.get('label')
        img = request.FILES["image"] 
        pil_img = Image.open(img)
        cv_img = np.array(pil_img)

        ### vertical shift and ratio  
        vertical_shift_img = vertical_shift(cv_img , 0.5) 
        v_shift_url=get_URL(vertical_shift_img,"v_shift_img") 

        ###  horizontal shift and ratio  
        horizontal_shift_img = horizontal_shift(cv_img , 0.5) 
        h_shift_url =get_URL(horizontal_shift_img,"h_shift_img") 

        # ### Zooming
        zoom_img = zoom(cv_img, .1)
        zoom_url = get_URL(zoom_img ,"zoom_img") 

        ### horizontal Flip 
        horizontal_flip_img = horizontal_flip(cv_img, True) 
        h_flip_url = get_URL(horizontal_flip_img,"h_flip_img") 

        ### vertical Flip 
        vertical_flip_img = vertical_flip(cv_img,True) 
        v_flip_url = get_URL(vertical_flip_img,"h_flip_img") 

        ### Rotation
        rotate_img = rotation(cv_img, 30) 
        rotate_url = get_URL(rotate_img,"rotate_img") 

        ### MODING ...wrap ,nearest , reflect , constant
        special_mode_img = horizontal_shift_mode(cv_img, .5 ,'wrap')
        special_mode_url = get_URL(special_mode_img,"special_mode_img") 

        response={
            "status": 200 ,
            "message":"image Url data successfully found" ,
            "success":True,
            "data":[
                {
                    "label": "Horizontal Shift",
                    "url" : h_shift_url ,
                    "code" : "some code" 
                },
                {
                    "label": "Vertical Shift",
                    "url" : v_shift_url ,
                    "code" : "some code" 
                },
                {
                    "label": "Zoom",
                    "url" : zoom_url ,
                    "code" : "some code" 
                },
                {
                    "label": "Horizontal Flip",
                    "url" : h_flip_url ,
                    "code" : "some code" 
                },
                 {
                    "label": "Vertical Flip",
                    "url" : v_flip_url ,
                    "code" : "some code" 
                },
                {
                    "label": "Rotate",
                    "url" : rotate_url ,
                    "code" : "some code" 
                },
                {
                    "label": "Special Mode (Wrap,Nearest,Constant,Reflect)",
                    "url" : special_mode_url ,
                    "code" : "some code" 
                }
                
            ]
            
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



