from django.urls import path
from shop_home.views import home

urlpatterns = [
    path('home/', home, name='home'),
]
