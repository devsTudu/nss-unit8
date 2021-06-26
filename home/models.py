from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  slug = models.SlugField()
  intro = models.TextField()
  doc_link = models.CharField(max_length=400)
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date_added']
  

class Members(models.Model):
    Name = models.CharField(max_length=255)
    Roll_Number = models.CharField(max_length=9)
    Email = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=100, null=True)
    
    class Meta:
      ordering = ['Name']

    def __str__(self):
      return self.Name



class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
    