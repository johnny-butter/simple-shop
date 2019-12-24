import json
from celery import shared_task
from api.models import Order
from django.db.models import F
from django.db.models import Sum, Count


@shared_task
def count_sale_data():
    datas = Order.objects \
                 .values(shop_name=F('shop__name')) \
                 .annotate(price_sum=Sum(
                     'price'), qy_sum=Sum('qy'), order_count=Count('id'))

    with open('sale_report.json', 'a') as f:
        content = ['{}\n'.format(json.dumps(data)) for data in datas]
        f.writelines(content)
