from django.contrib import admin

# Register your models here.
from .models import Post, Car, Members

admin.site.register(Post)
admin.site.register(Car)
admin.site.register(Members)

