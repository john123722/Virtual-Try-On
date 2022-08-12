from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from try_app import views

urlpatterns = [
    path("",views.index,name='index'),
    path("upload",views.upload,name = 'upload'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)