from django.urls import path
from .views import home, cake_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('cake/<int:cake_id>/', cake_detail, name='cake_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
