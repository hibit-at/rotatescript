from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse #追加


def index(request):#追加
    return HttpResponse('はろわ')#追加