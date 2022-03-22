from django.urls import path,re_path
from . import views

from rest_framework.routers import SimpleRouter

# router = SimpleRouter()




urlpatterns =  [
    path('add/',views.image_processing, name='add_resource_info'),
    ]