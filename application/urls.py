from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from application import views

urlpatterns = [
    url(r'^$',auth_views.LoginView.as_view(),name='login'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url(r'^register/$',views.register, name='register'),
    url(r'^profile/$',views.profile, name='profile'),
]
