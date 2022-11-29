from django.contrib.admin.sites import DefaultAdminSite
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))
