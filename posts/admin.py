from django.contrib import admin

# Register your models here.
from .models import articles, videos, photos, research

admin.site.register(articles)
admin.site.register(videos)
admin.site.register(photos)
admin.site.register(research)