from django.contrib import admin

# Register your models here.
from .models import article, video, photo, research, blog

admin.site.register(article)
admin.site.register(video)
admin.site.register(photo)
admin.site.register(research)
admin.site.register(blog)