from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('testDemo/', views.testDemo, name='testDemo'),
    path('userList/', views.userList, name='userList'),
    path('login/', views.login, name='login'),  # add this new URL path
    path('signup/', views.signup, name='signup'),  # add this new URL path
]
