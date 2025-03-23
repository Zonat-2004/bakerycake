from django.urls import path
from .views import home, cake_detail
from django.conf import settings
from django.conf.urls.static import static
from .views import cake_list
from django.conf import settings
from .views import custom_login


urlpatterns = [
    path('', home, name='home'),
    path('cakes/<int:cake_id>/', cake_detail, name='cake_detail'),
    path('cakes/', cake_list, name='cake_list'),
    path('login/', custom_login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
