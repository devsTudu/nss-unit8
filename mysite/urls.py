
from django.contrib import admin
from django.urls import path
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 


from posts.views import *
from home.views import homepage, post_detail, seeMembers, updateMembers

urlpatterns = [
  path('',homepage,name='NSS Unit 8'),
    path('admin/', admin.site.urls), 
    path('gallery/',showgallery,name='NSS Gallery'),
    path('members/',seeMembers,name='NSS Members'),
    path('articles/',showarticles,name='Articles'),  
    path('videos/',showvideos,name='NSS Members'),
    path('update',updateMembers, name='updating_wait'),
    path('<slug:slug>/', post_detail, name='post_detail'),
    path('posts/<slug:slug>/',articledetail, name="Article_detail")
    #path('covid_database/',covid_database,name='covid_database'),
    #path('blogs/',showblogs,name='NSS Members'), 
    #path('research/',showresearch,name='NSS Members'),
 
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
