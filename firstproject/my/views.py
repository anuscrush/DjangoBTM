from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    s="welcome to django session"
    return HttpResponse(s)

def view2(request):
    a="first class"
    return HttpResponse(a)

