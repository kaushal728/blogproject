from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=200)
    desc = models.TextField()

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default= 'default.jpg', upload_to='profile_pics')

    def __str__(self):
        return (f'{self.user.username} Profile')


