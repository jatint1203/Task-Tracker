from django.shortcuts import render

from rest_framework.decorators import api_view 
 
from rest_framework.response import Response
from api.serializer import TodoModelSerializer
from api.models import Task

# Create your views here.
@api_view(['GET'])
def APIoverview(requests):
    api_urls = {

     'List' : ' /task-list/' ,
'View' : '/detail-view/',
'Create' : 'task-create/' ,
'Update': '/task-update/<str>',
'Delete' : 'task-delete/<str>' ,

   }
    
    return Response(api_urls)
 
@api_view(['GET'])
def task_list(request):
    query = Task.objects.all().order_by('-id').values()
    serializer = TodoModelSerializer(query, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    
    serializer = TodoModelSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def one_task(request, pk):
    query = Task.objects.get(id=pk)
    serializer = TodoModelSerializer(query, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_update(request, pk):
    query = Task.objects.get(id=pk)
    
    serializer = TodoModelSerializer(instance=query,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

 
@api_view(['DELETE', 'GET'])
def task_delete(request, pk):
    print(pk)
    query = Task.objects.get(id=pk)
    print(query)
    query.delete()

    return Response("Item Deleted Successfully")
   


