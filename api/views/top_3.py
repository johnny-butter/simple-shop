from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.db.models import F
from django.db.models import Sum
from api.models import Order


class top_3(ViewSet):

    def list(self, request, *args, **kwargs):
        data = Order.objects \
                    .values(product_name=F('product__name'),
                            shop_name=F('shop__name')) \
                    .annotate(qy_sum=Sum('qy')) \
                    .order_by('-qy_sum')[:3]

        return Response(data=data, status=status.HTTP_200_OK)
