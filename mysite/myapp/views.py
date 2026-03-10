from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def home(request):
    item_list = Item.objects.all()
    context = {
        "item_list":item_list    
        }
    return render(request,"myapp/index.html",context)


def details(request,id):
    item = Item.objects.get(id=id)
    context = {
        "item" : item
    }
    return render(request,"myapp/details.html",context)
