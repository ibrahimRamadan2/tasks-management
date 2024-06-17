from rest_framework import serializers  
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            second_name=validated_data['second_name'],
            role=validated_data['role'],
            job_title=validated_data['job_title'],
            description=validated_data['description'],
            is_activated=validated_data.get('is_activated', False),
            is_deleted=validated_data.get('is_deleted', False),
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
 

