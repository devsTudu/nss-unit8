
from django.contrib import admin
from django.urls import path, include

from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from home.views import homepage, post_detail, showgallery, seeMembers

urlpatterns = [
    path('admin/', admin.site.urls), 
    #path('',views.index,name='index'),
    path('gallery/',showgallery,name='NSS Gallery'),
    path('members/',seeMembers,name='NSS Members'), 
    path('',homepage,name='NSS Unit 8'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]