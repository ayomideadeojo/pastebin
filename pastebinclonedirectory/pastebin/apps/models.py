from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone 
from django.contrib.auth import get_permission_codename


#this is the class model I used to which contains post the title, contents, etc
class Post(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE,null=True) #author has a private key as well
	private = models.BooleanField(default=False)




