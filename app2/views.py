from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def stringthree(request):
    return HttpResponse('<marquee><h2>Third String</marquee></h2>')

def stringfour(request):
    return HttpResponse('<marquee><ol><li>The Fourth String</li> <li> the next string</li></ol></marquee>')
