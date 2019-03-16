from django.urls import path,include,re_path
from django.conf.urls import url
from apps import views
from django.contrib import admin
from django.contrib.auth.views import (
PasswordResetView,
PasswordResetConfirmView,
PasswordResetDoneView,
PasswordResetCompleteView,
PasswordChangeView,
PasswordChangeDoneView,
)

urlpatterns = [
	path('',views.home,name='home'),
	path('accounts/', include('django.contrib.auth.urls'),name='login'),
	path('signup/',views.signup,name='signup'),
	path('accounts/profile/',views.profile,name='profile'),
	path('logout',views.logout_view,name='logout'),
	path('userpostnew', views.userpostnew, name='userpostnew'),
	path('admin', admin.site.urls, name='admin'),
	path('post-list/',views.post_list_admin,name='post-list'),
	re_path(r'^edit-post/(?P<pk>\d+)/$',views.edit_post,name='edit-post'),
	re_path(r'^delete-post/(?P<pk>\d+)/$',views.delete_post,name='delete-post'),
	re_path(r'^edit-profile/(?P<pk>\d+)/$',views.editprofile,name='edit-profile'),
	re_path(r'^delete-profile/(?P<pk>\d+)/$',views.deleteprofile,name='delete-profile'),
	re_path(r'^results/$',views.search,name='search'),

	re_path(r'^password_reset/$', PasswordResetView.as_view(), name='password-reset'),
    re_path(r'^password_reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/done/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),



]
