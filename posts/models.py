from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class article(models.Model):
  title = models.CharField(max_length=200)
  Contributors = models.CharField(max_length=500)
  slug = AutoSlugField(populate_from='title')

  intro = models.TextField()
  TYPE_CHOICES = (
        ('State','State'),
        ('National','National'),
        ('Regional','Regional')
    )

  TEXT_LANG = (
        ('English', 'English'),
        ('Hindi','Hindi'),
        ('Urdu','Urdu'),
        ('Bengali','Bengali'),
        ('Marathi','Marathi'),
        ('Odia','Odia'),
        ('Telgu','Telgu'),
        ('Tamil','Tamil')
    )
  Article_type = models.CharField(choices=TYPE_CHOICES,default='National',max_length=20)
  Language = models.CharField(choices=TEXT_LANG,default='English',max_length=20)
  photo = models.ImageField(upload_to='photos',blank=True, null=True)
  Link_to_Published_Doc = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
    ordering = ['-date_added']
  
  def __str__(self): 
        return self.title

class video(models.Model):
  title = models.CharField(max_length=200)
  Contributors = models.CharField(max_length=500)
  slug = models.SlugField()
  intro = models.TextField()
  Link_to_DriveVideo = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['-date_added']

  def __str__(self): 
        return self.name

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