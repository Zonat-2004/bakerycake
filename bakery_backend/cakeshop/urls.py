from django.urls import path
from .views import home, cake_detail
from django.conf import settings
from django.conf.urls.static import static
from .views import cake_list
from django.conf import settings


urlpatterns = [
    path('', home, name='home'),
    path('cakes/<int:cake_id>/', cake_detail, name='cake_detail'),
    path('cakes/', cake_list, name='cake_list')
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
