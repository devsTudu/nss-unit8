from django.shortcuts import render, HttpResponse,redirect


def index(request):
    return render(request,'home.html')

def home(request):
  return HttpResponse("Hello Debasish")