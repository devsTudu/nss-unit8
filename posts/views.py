from django.shortcuts import render
from .models import *

def showarticles(request):
  objects = article.objects.all()
  return render(request,'articles.html',{'list':objects})

def showresearch(request):
  objects = research.objects.all()
  return render(request,'research.html',{'list':objects})

def showvideos(request):
  objects = video.objects.all()
  return render(request,'videos.html',{'list':objects})

def showgallery(request):
  objects = photo.objects.all()
  return render(request,'gallery.html',{'list':objects})

def showblogs(request):
  objects = blog.objects.all()
  return render(request,'blogs.html',{'list':objects})


def articledetail(request, slug):
  q = article.objects.filter(slug__iexact = slug)
  if q.exists():
     q = q.first()
  else:
      return HttpResponse('<h1>Post Not Found</h1>')
   #return render(request, 'posts/details.html', context)
    
  return render(request, 'readingpages/readarticle.html', {'object': q})