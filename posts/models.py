from django.db import models

# Create your models here.
class article(models.Model):
  title = models.CharField(max_length=200)
  Contributors = models.CharField(max_length=500)
  slug = models.SlugField()
  intro = models.TextField()
  photo = models.ImageField(upload_to='photos',null=True)
  Link_to_Published_Doc = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date_added']

class video(models.Model):
  title = models.CharField(max_length=200)
  Contributors = models.CharField(max_length=500)
  slug = models.SlugField()
  intro = models.TextField()
  Link_to_DriveVideo = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date_added']

class research(models.Model):
  title = models.CharField(max_length=200)
  Contributors = models.CharField(max_length=500)
  slug = models.SlugField()
  photo = models.ImageField(upload_to='photos')
  intro = models.TextField()
  Link_to_Published_Doc = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date_added']

class photo(models.Model):
  Title = models.CharField(max_length=255)
  Contributors = models.CharField(max_length=500)
  Story = models.TextField()
  photo = models.ImageField(upload_to='photos')
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date_added']

class blog(models.Model):
  title = models.CharField(max_length=200)
  Contributors = models.CharField(max_length=500)
  slug = models.SlugField()
  intro = models.TextField()
  photo = models.ImageField(upload_to='photos')
  Link_to_blog = models.CharField(max_length=1000)
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date_added']