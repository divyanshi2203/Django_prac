from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def home(request):
    return HttpResponse("This is my new app.")

def details(request):
    item_list = Item.objects.all()
    context = {
        "item_list":item_list    
        }
    return render(request,"myapp/details.html",context)
