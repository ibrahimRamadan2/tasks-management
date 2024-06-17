from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class UserView(APIView):
    
    def get(self,request):
        users = User.objects.filter(is_deleted=False) 
        users_serializer = UserSerializer(users , many=True)
        return Response(users_serializer.data , status=status.HTTP_200_OK)
    
    def post(self,request):
        user_serializer = UserSerializer(data=request.data)
        if not user_serializer.is_valid():
             return Response(user_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        user_serializer.save() 
        return Response(user_serializer.data , status=status.HTTP_201_CREATED)

class UserDetailsView(APIView):
    def put(self,request,id):
        try:
            user = User.objects.get(id=id, is_deleted=False)
            user_serializer = UserSerializer(user , data=request.data , partial=True)
            if not user_serializer.is_valid():
                return Response(user_serializer.errors , status=status.HTTP_400_BAD_REQUEST)
            user_serializer.save() 
            return Response(user_serializer.data , status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"msg":f"User with id={id} Doesn't Exists!"} , status=status.HTTP_400_BAD_REQUEST)
            
    
    def delete(self,request,id):
        try:
            user = User.objects.get(id=id, is_deleted=False) 
            user.is_deleted = True 
            user.save() 
            return Response({"msg": "User Delete Sucessfully"} , status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"msg":f"User with id={id} Doesn't Exists!"} , status=status.HTTP_400_BAD_REQUEST)
            
