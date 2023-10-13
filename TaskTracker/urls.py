from django.contrib import admin
from django.urls import path, include
from TaskTracker import views

urlpatterns = [
    
  
    path('', views.index, name='index'),
    path('create_task', views.create_task, name='create_task'),
    path('update_task', views.update_task, name='update_task'),
]