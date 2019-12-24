from django.urls import path
from api.views import order, top_3

urlpatterns = [
    path('order/', order.as_view({'get': 'list',
                                  'post': 'create'}), name='order'),
    path('order/<int:pk>/',
         order.as_view({'delete': 'destroy'}), name='order_id'),
    path('top_3/', top_3.as_view({'get': 'list'}), name='top_3'),
]
