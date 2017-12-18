"""ingenius URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','reg.views.home',name='home'),
    url(r'^login/?$','reg.views.login_user',name='login'),
    url(r'^logout/?$','reg.views.logout_user',name='logout'),
    url(r'^register/?$','reg.views.register',name='register'),
    url(r'^breakfast/?$','reg.views.breakfast',name='breakfast'),
    url(r'^lunch/?$','reg.views.lunch',name='lunch'),
    url(r'^dinner/?$','reg.views.dinner',name='dinner'),
    url(r'^check_in/?$','reg.views.check_in',name='check_in'),
    url(r'^stats/?$','reg.views.stats',name='stats'),
    url(r'^dashboard/?$','reg.views.dashboard',name='dashboard'),
]
