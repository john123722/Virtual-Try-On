from django.shortcuts import render
from django import views
from django.urls import is_valid_path
from .forms import ImageForm
from .models import Image


def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
    form = ImageForm()
    img = Image.objects.last()
    return render(request,'index.html',{'img':img ,'form':form})



def upload(request):
    return render(request,'upload.html') 




