from django.shortcuts import render

# Create your views here.

def index(requests):
    return render(requests, 'index.html')

def create_task(requests):
    return render(requests, 'create_task.html')

def update_task(requests):
    return render(requests, 'update_task.html')


