from django.db import models
from pymongo import MongoClient
from django.conf import settings

client = MongoClient("mongodb://localhost:27017/")
db = client.get_database("QuanLyWebBanBanh")  # Dùng dấu ngoặc tròn ()
client = MongoClient(settings.MONGO_URI)  # Lấy URL kết nối từ settings.py
cakes_collection = db["cakes"]  # Lấy collection cakes
categories_collection = db["categories"]

# class Cake(models.Model):
#     name = models.CharField(max_length=255, verbose_name="Tên bánh kem")
#     description = models.TextField(blank=True, null=True, verbose_name="Mô tả")
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Giá bán")
#     image = models.ImageField(upload_to='cakes/', blank=True, null=True, verbose_name="Ảnh sản phẩm")
class Cake:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description