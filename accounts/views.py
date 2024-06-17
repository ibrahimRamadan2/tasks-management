from django.shortcuts import render
from rest_framework.views import APIView
from .models import User , UserToken
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import send_confirmation_mail
from django.db import transaction
import uuid
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
        try: 
            with transaction.atomic():
                user_serializer.save() 
                user= User.objects.get(id=user_serializer.data['id'])
                user_token = UserToken.objects.create(user=user , token = uuid.uuid4())
                user_token.save()
                send_confirmation_mail(user_serializer.data['email'],user_token.token)
                return Response(user_serializer.data , status=status.HTTP_201_CREATED)
                
        except Exception as e :
            print(e) 
            return Response({"msg": "Something wrong happened"} ,status=status.HTTP_400_BAD_REQUEST ) 

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
            


class UserConfirmationView(APIView):
    
    def post(self,request, token):
        try:  
            user_token = UserToken.objects.get(token=token )
            user = user_token.user
            user.is_activated = True 
            user.save()  
            return Response({"msg":"User email confirmed sucessfully"} , status=status.HTTP_200_OK)
        except UserToken.DoesNotExist:
            return Response({"msg": "user token is invalid"} ,status=status.HTTP_404_NOT_FOUND ) 
        except:
            return Response({"msg": "Something wrong happened"} ,status=status.HTTP_400_BAD_REQUEST ) 
            
        