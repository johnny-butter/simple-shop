from rest_framework import status
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import APIException


class VipOnly(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('the product can only buy as VIP user')
    default_code = 'vip_001'


class StockNotEnough(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('stock is not enough')
    default_code = 'stock_001'
