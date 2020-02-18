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
#from kicken import urls as kicken_urls

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('botlist/', views.botlist),
    path('projekt47/', include('projekt47.urls')),
    url(r'^', include('django_telegrambot.urls')),
    #url(r'^parser/', include('mensaparser.urls')),
    #path('kicken/', include('kicken.urls')),
]
