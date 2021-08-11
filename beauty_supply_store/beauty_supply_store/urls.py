
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from products.views import *
from cart.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', home, name='home'),
    path('category/<id>/', category, name='category'),
    path('product/<id>/', product_id, name="product_id"),
    path('login/', login_user , name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', register_user, name="register"),
    path('search/', search, name='search'),
    path('contact/', contact, name='contact'),
    path('password/', change_password, name='change_password'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
