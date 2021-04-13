from django.shortcuts import render, HttpResponse,redirect

from .models import Post

from .forms import CommentForm
from .models import Post

def homepage(request):
  posts = Post.objects.all()
  return render(request,'index.html',{'posts':posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'readblog.html', {'post': post, 'form': form})

def showgallery(request):
  return render(request,'gallery.html')

def seeMembers(request):
  return render(request,'members.html')
