from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='static/mementos_files/images', default='')

    def __str__(self):
        return self.user.username


class Memento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # A field for creating a one-to-many relationship with another model
    published_date = models.DateField(auto_now_add=True) # A field for storing a date value
    title = models.CharField(max_length=75)
    text = models.TextField(max_length=250)
    img1 = models.ImageField(upload_to='static/mementos_files/images', blank=True, default='')
    img2 = models.ImageField(upload_to='static/mementos_files/images', blank=True, default='')
    img3 = models.ImageField(upload_to='static/mementos_files/images', blank=True, default='')
    audio = models.FileField(upload_to='static/mementos_files/audios', default='') # A field for storing an audio

    def __str__(self):
        return f"{self.title} - {self.user}"