from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone 
from django.contrib.auth import get_permission_codename

class Post(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	private = models.BooleanField(default=False)




