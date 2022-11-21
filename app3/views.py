from django.shortcuts import render
from django.urls import HttpResponse
# Create your views here.
def wish(reqest):
    return HttpResponse('hello dear my project')


