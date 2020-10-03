from django.contrib import admin
from .import views
from django.conf.urls import url,include

from django.urls import path,re_path

urlpatterns = [

    #path('',views.index,name="index"),
    path('',views.blog_title,name="blog_title"),
    re_path(r'(?P<article_id>\d)/$',views.blog_article,name="blog_detail"),
]
