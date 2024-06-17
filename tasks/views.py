from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response
from rest_framework import status

from .models import Tasks 
from .serializers import TasksSerilizer

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TaskView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        tasks = Tasks.objects.filter(is_deleted=False)
        serialized_data = TasksSerilizer(tasks,many=True)
        return Response({"msg":serialized_data.data} , status=status.HTTP_200_OK) 
    
    def post(self,request):
        task_serializer =  TasksSerilizer(data=request.data)
        if task_serializer.is_valid(): 
            task_serializer.save()
            return Response(task_serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(task_serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class TaskDetailsView(APIView):
    def put(self,request, id):
        try:
            task =Tasks.objects.get(id=id, is_deleted=False)
            task_serializer =  TasksSerilizer(task, data=request.data, partial=True)
            if task_serializer.is_valid(): 
                task_serializer.save()
                return Response(task_serializer.data , status=status.HTTP_200)
            else:
                return Response(task_serializer.errors , status=status.HTTP_400_BAD_REQUEST)        
        except Tasks.DoesNotExist:
            return Response({"msg": f"Task with Id {id} Doesn't Exists!"} , status=status.HTTP_404_NOT_FOUND)        
            
 
    def delete(self,request, id):
        try:
            task =Tasks.objects.get(id=id, is_deleted=False)
            task.is_deleted = True
            task.save() 
            return Response({"msg": "Task Deleted"}, status=status.HTTP_200_OK)
        except Tasks.DoesNotExist:
            return Response({"msg": f"Task with Id {id} Doesn't Exists!"} , status=status.HTTP_404_NOT_FOUND)  


    
