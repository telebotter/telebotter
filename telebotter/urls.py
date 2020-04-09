"""telebotter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('botlist/', views.botlist),
    path('projekt47/', include('projekt47.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/login.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    # path('login/', views.tglogin, name='login'),
    path('login/verify', views.tglogin_verify),
    url(r'^', include('django_telegrambot.urls')),
    #url(r'^parser/', include('mensaparser.urls')),
    #path('kicken/', include('kicken.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
