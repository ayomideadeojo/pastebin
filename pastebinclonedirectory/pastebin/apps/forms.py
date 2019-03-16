from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#class from for users to post this allows for title,content, and private settings
class Userpostform(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','content','private')
    

class Visitorpostform(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','content')
#class for user registration form this has 4 fields, username,email,password,password2
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

