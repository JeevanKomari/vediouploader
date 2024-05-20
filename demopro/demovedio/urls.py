from django.urls import path
from . import views
urlpatterns = [
path('uploadfile', views.UploadFile, name='UploadFile'),
]