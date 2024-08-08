from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('testDemo/', views.testDemo, name='testDemo'),
]
