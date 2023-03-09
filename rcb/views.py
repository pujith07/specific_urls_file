from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kholi(request):
    return HttpResponse('<h1><marquee>Kholi is the best batsman</h1></marquee>')
def abd(request):
    return HttpResponse('<h1><marquee>Abd is called as mr.360</h1></marquee>')