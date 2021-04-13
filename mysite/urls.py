
from django.contrib import admin
from django.urls import path

from home.views import homepage, post_detail, showgallery, seeMembers

urlpatterns = [
    path('admin/', admin.site.urls), 
    #path('',views.index,name='index'),
    path('gallery/',showgallery,name='NSS Gallery'),
    path('members/',seeMembers,name='NSS Members'), 
    path('',homepage,name='NSS Unit 8'), 

    path('<slug:slug>/', post_detail, name='post_detail'),
]