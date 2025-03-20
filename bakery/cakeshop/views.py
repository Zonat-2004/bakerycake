from django.shortcuts import render, get_object_or_404
from .models import Cake
from pymongo import MongoClient
from bson import ObjectId
client = MongoClient('mongodb://localhost:27017/')  # Your MongoDB connection string
db = client.QuanLyWebBanhKem  # Your MongoDB database name

def home(request):
    cakes = Cake.objects.all()
    return render(request, 'cakeshop/home.html', {'cakes': cakes})

def cake_detail(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    return render(request, 'cakeshop/cake_detail.html', {'cake': cake})
