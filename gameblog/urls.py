from django.urls import path
from .views import *

app_name = 'gameblog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<str:slug>/', post_details, name='post_details'),
]