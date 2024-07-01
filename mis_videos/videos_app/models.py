from django.db import models
    
# Create your models here.

class user_data(models.Model):
    id_user= models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)

class videos_data(models.Model):
    id_video = models.IntegerField()
    video_name = models.CharField(max_length=50)
    video_extension = models.CharField(max_length=5)
    video_size = models.IntegerField()
    video_url = models.URLField()

class videos_users(models.Model):
    id_video = models.IntegerField()
    id_user= models.CharField(max_length=10)

class video_number(models.Model):
    id_user= models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    numero_de_video = models.IntegerField()

