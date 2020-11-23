from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .views import FileView
urlpatterns = [
    path('',getprojectpdata,name='getprojectpdata'),
    path('project_detail/<int:pk>',project_detail,name='project_detail'),
    path('project/', ProjectView.as_view(), name='ProjectView'),
    path('project/<int:pk>', ProjectupdateView.as_view(), name='project'),
    path('scan/',Scans,name='Scans'),
    path('scan_detail/<int:pk>',scan_detail,name='scan_detail'),
    
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)