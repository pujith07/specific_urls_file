from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dhoni(request):
    return HttpResponse('<h1><marquee>dhoni is best finisher</marquee></h1>')
def raina(request):
    return HttpResponse('<h1><marquee>Raina is called as mr.ipl</h1></marquee>')