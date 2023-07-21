from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def stringone(request):
    return HttpResponse('the response')

def stringtwo(request):
    return HttpResponse('<marquee><h1> The second String</marquee></h1>')