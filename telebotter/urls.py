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
import logging
#from kicken import urls as kicken_urls

logger = logging.getLogger()

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('botlist/', views.botlist),
    url(r'^', include('django_telegrambot.urls')),
    #url(r'^parser/', include('mensaparser.urls')),
]


try:
    urlpatterns.append(
        path('kicken/', include('kicken.urls')))
except ModuleNotFoundError as e:
    logger.exception('Kicken urls nicht geladen')
