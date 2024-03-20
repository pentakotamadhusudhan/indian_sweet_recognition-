from django.db import models
from django.contrib.auth.models import User

class UploadedImage(models.Model):
    user = models.ForeignKey(User, related_name='user',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


