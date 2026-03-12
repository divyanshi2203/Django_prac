from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('',views.home,name = "home"),
    path('details/<int:id>/',views.details,name = "details"),
    path('add/',views.create_item,name='create_item'),
]