from django.contrib import admin
from django.urls import path
from articles.views import sport

urlpatterns = [
    path('<str:category>/<int:article_id>', sport, name = 'category'),
]
