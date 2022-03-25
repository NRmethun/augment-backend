from django.urls import path,re_path
from . import views
from rest_framework.routers import SimpleRouter

urlpatterns =  [
    path('augment/',views.image_processing, name='add_resource_info'),
    ]