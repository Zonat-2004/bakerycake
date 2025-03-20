from django.db import models

class Cake(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tên bánh kem")
    description = models.TextField(blank=True, null=True, verbose_name="Mô tả")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Giá bán")
    image = models.ImageField(upload_to='cakes/', blank=True, null=True, verbose_name="Ảnh sản phẩm")

    def __str__(self):
        return self.name
