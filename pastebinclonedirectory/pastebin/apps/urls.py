from django.urls import path,include
from apps import views
urlpatterns = [
	path('',views.home,name='home'),
	path('accounts/', include('django.contrib.auth.urls'),name='login'),
	path('signup',views.signup,name='signup'),
]
