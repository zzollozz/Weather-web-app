from django.urls import path
from authapp.views import logout
from django.contrib import admin

app_name = 'authapp'

urlpatterns = [

    path('logout/', logout, name='logout')
]
