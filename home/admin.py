from django.contrib import admin

# Register your models here.
from .models import Post, Members

admin.site.register(Post)
admin.site.register(Members)

