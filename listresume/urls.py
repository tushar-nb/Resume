from django.contrib import admin
from django.urls import path, include

import editresume
from . import views


urlpatterns = [
    path('', views.ListResume, name='listresume'),
    path('<int:id>/edit/',include('editresume.urls')),   
    path('<int:id>/delete/',views.DeleteResume, name='delete'),   
    path('<int:id>/view/', views.ViewResume, name='viewresume'),

]