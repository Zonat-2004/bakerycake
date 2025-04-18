from django.shortcuts import render, get_object_or_404
from .models import Cake
from pymongo import MongoClient
from bson import ObjectId
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.conf import settings
from .models import cakes_collection, categories_collection  # Import collection từ models

client = MongoClient('mongodb://localhost:27017/')  # Your MongoDB connection string
db = client.QuanLyWebBanhKem  # Your MongoDB database name

def cake_list(request):
    cakes = list(cakes_collection.find())  # Lấy danh sách bánh từ MongoDB
    categories = list(categories_collection.find())  # Lấy danh sách categories

    # Chuyển ObjectId thành string và xử lý đường dẫn hình ảnh
    for cake in cakes:
        cake["_id"] = str(cake["_id"])
        if "image" in cake:
            # Đảm bảo đường dẫn hình ảnh bắt đầu bằng MEDIA_URL
            if not cake["image"].startswith(settings.MEDIA_URL):
                cake["image"] = f"{settings.MEDIA_URL}{cake['image']}"

    return render(request, 'cakeshop/cakes.html', {'cakes': cakes, 'categories': categories})

def home(request):
    cakes = list(cakes_collection.find())  # Lấy danh sách bánh từ MongoDB

    # Chuyển ObjectId thành string và xử lý đường dẫn hình ảnh
    for cake in cakes:
        cake["_id"] = str(cake["_id"])
        if "image" in cake:
            if not cake["image"].startswith(settings.MEDIA_URL):
                cake["image"] = f"{settings.MEDIA_URL}{cake['image']}"

    return render(request, 'cakeshop/home.html', {'cakes': cakes})
def custom_login(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        password = request.POST["password"]
        user = authenticate(request, username=phone, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Chuyển hướng sau khi đăng nhập thành công
        else:
            messages.error(request, "Số điện thoại hoặc mật khẩu không đúng!")

    return render(request, "cakeshop/login.html")


def cake_detail(request, cake_id):
    cake = get_object_or_404(Cake, id=cake_id)
    return render(request, 'cakeshop/cake_detail.html', {'cake': cake})
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Đăng ký thành công! Hãy đăng nhập.")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'cakeshop/register.html', {'form': form})
def search_view(request):
    query = request.GET.get("q", "")
    results = []

    if query:
        results_cursor = cakes_collection.find({
            "name": {"$regex": query, "$options": "i"}
        })
        results = list(results_cursor)  # Chuyển cursor thành list

        # Xử lý ảnh cho kết quả tìm kiếm
        for cake in results:
            cake["_id"] = str(cake["_id"])
            if "image" in cake and not cake["image"].startswith(settings.MEDIA_URL):
                cake["image"] = f"{settings.MEDIA_URL}{cake['image']}"

    return render(request, 'cakeshop/search_results.html', {
        'query': query,
        'results': results
    })
