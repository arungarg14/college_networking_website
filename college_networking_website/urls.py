"""college_networking_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings
from application import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    url(r'^register/$',views.register, name='register'),
    url(r'^profile/$',views.profile, name='profile'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # url(r'^',include('application.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
