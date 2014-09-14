from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import os
from django import forms

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class ImageUploadForm(forms.Form):
    photo = forms.ImageField()

class Post(models.Model):
	username = models.CharField(max_length=400)
	text = models.CharField(max_length=400)
	photo = models.FileField(upload_to='%Y/%m/%d', blank=True, null=True)
	expiration = models.DateTimeField('expiration date')
	
class Follow(models.Model):
	username = models.CharField(max_length=400)
	following = models.CharField(max_length=400)
