from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
   
    path('', views.APIoverview, name='APIoverview' ),
    path('task_list', views.task_list, name='task_list' ),
    path('task_create', views.task_create, name='task_create' ),
    path('task_update/<str:pk>/', views.task_update, name='task_update' ),
    path('task_delete/<str:pk>/', views.task_delete, name='task_delete' ),
    path('one_task/<str:pk>/', views.one_task, name='one_task' ),
]
