from asyncio.windows_events import NULL
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
    if Image.objects.count() >0 :
        max_id = Image.objects.latest('id').id
        img = Image.objects.filter(id = max_id)
        return render(request,'index.html',{'img':img ,'form':form})
        
    else:
        img = Image.objects.all()
        return render(request,'index.html',{'img':img ,'form':form})



def upload(request):
    return render(request,'upload.html') 




