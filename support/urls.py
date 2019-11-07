from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('<str:option>', views.index, name = 'index'),
]
