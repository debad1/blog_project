from django.contrib import admin
from django.urls import path, include
from blog_project.views import home

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home, name='index'),
    path('category/', include("articles.urls")),
]
