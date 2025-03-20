from django.urls import path
from .views import home, cake_detail

urlpatterns = [
    path('', home, name='home'),
    path('cake/<int:cake_id>/', cake_detail, name='cake_detail'),
]
