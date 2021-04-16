from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  slug = models.SlugField()
  intro = models.TextField()
  body = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date_added']
  

class Members(models.Model):
    Name = models.CharField(max_length=255)
    Roll_Number = models.CharField(max_length=9)
    FB_Handle = models.CharField(max_length=100)
    Insta_Id = models.CharField(max_length=100)
    Twitter = models.CharField(max_length=100)
    LinkedIn = models.CharField(max_length=100)
    image = models.ImageField(upload_to='MembersPhoto')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
    