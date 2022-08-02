from email.mime import image
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import redirect, render
from myapp.models import *
from  django.shortcuts import redirect 

def show_about_page(request):
    print("page ")
    return render(request, 'about.html')

def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data ={'images': images,'cats':cats}
    return render(request,'home.html',data)

def show_category_page(request,cid):
    print(cid)
    cats = Category.objects.all()
    
    cat = Category.objects.get(pk=cid)
    print(cat)
    
    
    images = Image.objects.filter(cat=cat)
    data ={'images': images,'cats':cats}
    return render(request,'home.html',data)

def home(request):
    return redirect('/home')