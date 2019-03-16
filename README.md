# pastebin
Pastebin Clone using Python/Django

By Ayomide Adeojo and Karan Naidu

This Project is meant to clone some of the functionalities of Pastebin 
I will brefiely describe the layout of the project

A pastebin app was created with the folder
within this folder an apps folder was created which holds
admin.py,apps.py,forms.py,models.py,test.py,urls.py,and views.py
Most of the functionality is witin this folder

I will describe what is located within some of these python files

Views
apps/views.py 
the views which the urls use are defined in this file, this included functions like userpostnew, deleteprofile,edit_post,delete_post, and search
I used a few views which are defined by 'django.contrib' this includes the Password Reset Functionality as well as Login and Logout.

Urls
urls.py
contains the admin/ path and initial empty parameter tags which includes apps.url 
apps/urls.py
Contains most of the path functionality for this project. Including paths to views such as signup,edituser,createpost etc

HTML CODE is Located within
apps/templates/app folder and apps/templates/registration folder
these contains html pages for home,logout,signup,profile,new post creations. base.html is the base html page common to most other pages
values are changed depending if use is authenticate or not

Database
the default sqlite database is used for this project as well.

Settings.py
an email backend was including to allow password resets though gmail
