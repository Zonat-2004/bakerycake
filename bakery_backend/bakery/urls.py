from django.contrib import admin
from django.urls import include, path
from cakeshop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', views.search_view, name='search'),
    path('', include('cakeshop.urls')),
]
