from django.urls import path,include,re_path
from django.conf.urls import url
from apps import views
from django.contrib import admin

urlpatterns = [
	path('',views.home,name='home'),
	path('accounts/', include('django.contrib.auth.urls'),name='login'),
	path('signup/',views.signup,name='signup'),
	path('accounts/profile/',views.profile,name='profile'),
	path('logout',views.logout_view,name='logout'),
	path('userpostnew', views.userpostnew, name='userpostnew'),
	path('admin', admin.site.urls, name='admin'),
	path('post-list/',views.post_list_admin,name='post-list'),
	re_path(r'^edit-post/(?P<pk>\d+)/$',views.edit_post,name='edit-post')


]
