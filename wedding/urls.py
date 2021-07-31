from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_images, name='wedding_list_images'),
]
