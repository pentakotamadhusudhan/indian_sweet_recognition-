from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import generics,status
from .predection_sweets import predict_image,class_names
from .forms import *
from .models import UploadedImage
# from djan
# class_names = ['gulab jamun','jelabi','kajja','kajju katli']
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image_path = r'D:\projects\MLproject\classfication_sweets\india_sweet_predections\sweets_classfications\downloaded_images\test\gulab juman\gulabjamun6.jpg'  # Replace with the path to your image
            daata = UploadedImage.objects.all().last()
            x = predict_image(img_path=daata.image.path)
            print(x)
            return HttpResponse(class_names[x])
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')


class ImageDetection(generics.GenericAPIView):

    serializer_class = ImageUploadSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        " find your favorite image"
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            daata = UploadedImage.objects.all().last()
            index = predict_image(img_path=daata.image.path)
            print(index)
            return Response({
                "result" : class_names[index], "status":status.HTTP_201_CREATED
            })
        except Exception as e:
            print(e)
            return Response({
                "result" : "error", "status":status.HTTP_400_BAD_REQUEST,"message":e.args
            })
        
    

class Login(generics.GenericAPIView):
    serializer_class  = LoginSerializer
   

    def post(self,request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            print(username,password)
            userdetails = User.objects.get(username = username)
            user = authenticate(request,username=username,password=password)
            if user:
                # token = RefreshToken()
                login(request=request,user=user)
                # toke = Token.objects.create(user=userdetails)
                # print("-----------------",toke)
                
                return Response({
                                "status":status.HTTP_200_OK,
                                'result' : User(user,context= {'request': request}).data,
                                "hasherror": True,
                                
                            })
            else:
                return Response({
                                "status":status.HTTP_404_NOT_FOUND,
                                'result' : [],
                                "hasherror": True
                            })
        except Exception as e:
                return Response({
                                "status":status.HTTP_500_INTERNAL_SERVER_ERROR,
                                'result' : [],
                                "hasherror": True
                            })

