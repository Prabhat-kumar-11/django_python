from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('greet/<str:username>', views.greet, name='greet'),
    path('farewell/<str:username>', views.farewell, name='farewell'),
]