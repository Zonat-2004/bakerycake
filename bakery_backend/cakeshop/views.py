from django.shortcuts import render, get_object_or_404
from .models import Cake
from pymongo import MongoClient
from bson import ObjectId
from django.conf import settings
from .models import cakes_collection, categories_collection  # Import collection từ models
client = MongoClient('mongodb://localhost:27017/')  # Your MongoDB connection string
db = client.QuanLyWebBanhKem  # Your MongoDB database name

def cake_list(request):
    cakes = list(cakes_collection.find())  # Lấy danh sách bánh từ MongoDB
    categories = list(categories_collection.find())  # Lấy danh sách categories

    # Chuyển ObjectId thành string (nếu có)
    for cake in cakes:
        if "image" in cake and not cake["image"].startswith(settings.MEDIA_URL):
            cake["image"] = settings.MEDIA_URL + cake["image"]  # Dùng settings.MEDIA_URL
        cake["_id"] = str(cake["_id"])
        
    
    return render(request, 'cakes.html', {'cakes': cakes, 'categories': categories})

def home(request):
    cakes = list(cakes_collection.find())  # Lấy danh sách bánh từ MongoDB

    # Chuyển ObjectId thành string (vì Django không hiển thị ObjectId được)
    for cake in cakes:
        cake["_id"] = str(cake["_id"])

    return render(request, 'cakeshop/home.html', {'cakes': cakes})


def cake_detail(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    return render(request, 'cakeshop/cake_detail.html', {'cake': cake})
