from django.urls import path
from . import views
from .views import ImageDetection



urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('upload/success/', views.upload_success, name='upload_success'),
    path('up',ImageDetection.as_view())
]
