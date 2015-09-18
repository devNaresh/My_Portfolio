"""My_Blog URL Configuration

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
from front_page.views import index, blog_home,blog_search, blog_post

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^blog/$', blog_home.as_view(), name='blog_home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/search/',blog_search.as_view(),name='blog_search'),
    url(r'^blog/(?P<pk>[0-9]+)/',blog_post.as_view(),name='blog_post'),
    url(r'^blog/(?P<query>[a-zA-Z]+)/',blog_search.as_view(),name='blog_cat'),
]
