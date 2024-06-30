from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.Create,name='Create'),
    path('success/',views.Success, name='success'),
]
