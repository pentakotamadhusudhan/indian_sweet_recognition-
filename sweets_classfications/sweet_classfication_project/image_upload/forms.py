from django import forms
from rest_framework import serializers
from .models import UploadedImage
from django.contrib.auth.models import User

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ['image']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    


class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "username","password"