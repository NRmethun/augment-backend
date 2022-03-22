from logging import exception
from django.shortcuts import render

# Create your views here.


# from django.db.models.fields.related import _ChoiceNamedGroup
# from asyncio.windows_events import NULL
from distutils import extension
from sys import audit
from rest_framework import viewsets, parsers
from django.http import response
from django.shortcuts import render

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sklearn import exceptions
from .models import ImageData

from rest_framework import viewsets
from django.db.models import Q
#from resource import serializers
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
@api_view(['POST'])
def get_content(request):
    try:
        label= request.POST.get('label')
        print('aa')
        img = request.FILES["image"] 
        # byteee = base64.b64decode(img)  


        pil_img = Image.open(img)
        cv_img = np.array(pil_img)
        img = get_filtered_image(cv_img,'bluring')

        img = (img) 
        # print(img) 

        # plt.imshow(img)
        # plt.show() 
        print('ssa')
        # byteee = base64.b64decode(img) 

        
        

        

        # with open(request.FILES["image"] , "rb") as image_file:
        #     encoded_string = base64.b64encode(image_file.read())

        # print(encoded_string) 
        # dlimage = requests.request("GET", imageURL)
        encodedImage =  base64.encodestring(img)




        # print(base64_message  )
        # plt.imshow(byteee)
        # plt.show() 
                            # uploaded_image = request.FILES['image']
                            # fs = FileSystemStorage()
                            # filename = fs.save(uploaded_image.name, uploaded_image)
                            # uploaded_file_url = fs.url(filename) 
        
        # code = get_code(uploaded_file_url)
        # response={
        #             "response_code": 200,
        #             "response_text": 'Data found successfully',
        #             "success": True,
        #             "data": img 

        #             }
        # response = {'uploaded_file_url': uploaded_file_url}

        return Response({"response":"response", "img": 'byteee' } )
    except  :
        # print(e) 
        response ={
                    "response_code" : 404,
                    "response_text" : 'failed to get Resources',
                    "success" : False,
                    "error":[ {
                        "message": "failed to get Resources",
                        "code":404
                    }]
                }

        return Response(response) 

from  .processing import horizontal_shift ,vertical_shift,zoom,horizontal_flip,vertical_flip,rotation,horizontal_shift_mode

from .color_processing import brightness
@api_view(['POST'])
def image_processing(request):

    label= request.POST.get('label')
    img = request.FILES["image"] 

    pil_img = Image.open(img)
    cv_img = np.array(pil_img)
    # ### vertical shift and ratio  
    # img = vertical_shift(cv_img , 0.5) 
    # ###  horizontal shift and ratio  
    # img = horizontal_shift(cv_img , 0.5) 
    # ### Zooming
    # img = zoom(cv_img, .1) 
    # ### horizontal Flip 
    # img = horizontal_flip(cv_img, True)
    # ### vertical Flip 
    # img = vertical_flip(cv_img,True) 
    # ### Rotation
    # img = rotation(cv_img, 30)
    ### MODING ...
    # img = horizontal_shift_mode(cv_img, .7 ,'nearest')
    ##### upto avobe geo translation 

    img = brightness(cv_img, 0.5, 3)
    
    plt.imshow(img)
    plt.show()  
    return 




