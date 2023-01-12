from django.urls import path
from .views import *

urlpatterns = [
    path('base/', base, name='base'),
    path('', home, name='home'),
    path('add_list/', add_list, name='add_list'),
    path('delete/<id>', delete, name='delete'),
    path('update/<id>', update, name='update'),
    path('list/<id>', insideItem, name='insideItem'),
    path('complete/<id>', complete, name='complete'),
    path('incomplete/<id>', incomplete, name='incomplete'),
]