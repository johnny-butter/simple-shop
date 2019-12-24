from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Order, Product
from api.serializers import OrderSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from functools import wraps
from django.db.models import F
from django.contrib.auth.models import AnonymousUser
from simple_shop.error_code import VipOnly, StockNotEnough


def vip_only(func):
    @wraps(func)
    def wrap(order, request, *args, **kwargs):
        product_id = request.POST.get('product')

        need_vip = Product.objects.get(id=product_id).vip

        if need_vip:
            if isinstance(request.user, AnonymousUser):
                raise VipOnly
            elif request.user.vip is False:
                raise VipOnly

        return func(order, request, *args, **kwargs)

    return wrap


def can_buy(func):
    @wraps(func)
    def wrap(order, request, *args, **kwargs):
        product_id = request.POST.get('product')
        purchase_amount = int(request.POST.get('qy'))

        stock_pcs = Product.objects.get(id=product_id).stock_pcs

        if stock_pcs <= 0 or stock_pcs < purchase_amount:
            raise StockNotEnough

        kwargs.update(
            {
                'product_id': product_id,
                'purchase_amount': purchase_amount,
            }
        )

        return func(order, request, *args, **kwargs)

    return wrap


class order(mixins.ListModelMixin, mixins.CreateModelMixin,
            mixins.DestroyModelMixin, GenericViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @vip_only
    @can_buy
    def create(self, request, *args, **kwargs):
        Product.objects.filter(id=kwargs['product_id']).update(
            stock_pcs=(F('stock_pcs') - kwargs['purchase_amount']))

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        product = instance.product

        data = {'before_amount': product.stock_pcs}

        product.stock_pcs += instance.qy
        product.save()

        data.update({'after_amount': product.stock_pcs})

        self.perform_destroy(instance)
        return Response(data=data, status=status.HTTP_200_OK)
