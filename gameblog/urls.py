from django.urls import path
from .views import *

app_name = 'gameblog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('news/<str:slug>/', post_details, name='post_details'),
    path('news/category/<int:category_id>', category_list, name='category_list')
]