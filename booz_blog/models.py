# ORM - Object Relational Mapper that creates SQL tables behind the scenes
from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


class Post(models.Model):
    image = models.ImageField(default='blank-drink-pic.jpg', upload_to='boozula_pix')
    title = models.CharField(max_length=100)
    main_alcohol = models.CharField(max_length=100)
    ingredients = models.TextField()
    preparation = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
    # "dunder" str method
    def __str__(self):
        return self.title
    
    # def save(self):
    #     super().save()
        
    #     img = Image.open(self.image.path)
        
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
            
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})