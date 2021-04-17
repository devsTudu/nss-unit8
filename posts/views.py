from django.shortcuts import render
from .models import *

def showarticles(request):
  objects = articles.objects.all()
  return render(request,'articles.html',{'list':objects})

def showresearch(request):
  objects = research.objects.all()
  return render(request,'research.html',{'list':objects})

def showvideos(request):
  objects = videos.objects.all()
  return render(request,'videos.html',{'list':objects})

def showgallery(request):
  objects = photos.objects.all()
  return render(request,'gallery.html',{'list':objects})

def showblogs(request):
  objects = blogs.objects.all()
  return render(request,'blogs.html',{'list':objects})


def articledetail(request, slug):
  q = articles.objects.filter(slug__iexact = slug)
  if q.exists():
     q = q.first()
  else:
      return HttpResponse('<h1>Post Not Found</h1>')
   #return render(request, 'posts/details.html', context)
    
  return render(request, 'readingpages/readarticle.html', {'object': q})