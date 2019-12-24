import random
from unittest import skip
from api.models import Order
from rest_framework.test import APITestCase
from api import factory


class OrderTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = factory.UserFactory.create()
        cls.vip_user = factory.VipUserFactory.create()

        cls.customer = factory.CustomerFactory.create()

        cls.product = factory.ProductFactory.create()
        cls.vip_product = factory.VipProductFactory.create()
        cls.no_stock_product = factory.ProductFactory.create(stock_pcs=0)

        order_qy = random.randint(1, 5)
        cls.order = factory.OrderFactory.create(
            product_id=cls.product.id,
            shop_id=cls.product.shop.id,
            qy=order_qy,
            price=cls.product.price * order_qy,
            customer_id=cls.customer.id
        )

    def test_user_can_not_buy_no_stock_product(self):
        response = self.client.post(
            '/api/order/',
            data={
                'product': self.no_stock_product.id,
                'qy': 1,
                'customer': self.customer.id,
            }
        )

        self.assertEqual(response.data.get('detail').get('code'),
                         'stock_001', response.data)

    def test_user_can_not_buy_vip_product(self):
        response = self.client.post(
            '/api/order/',
            data={
                'product': self.vip_product.id,
                'qy': 1,
                'customer': self.customer.id,
            }
        )

        self.assertEqual(response.data.get('detail').get('code'),
                         'vip_001', response.data)

    def test_user_can_buy_product(self):
        qy = random.randint(1, 5)
        before_stock_pcs = self.product.stock_pcs

        response = self.client.post(
            '/api/order/',
            data={
                'product': self.product.id,
                'qy': qy,
                'customer': self.customer.id,
            }
        )

        self.product.refresh_from_db()

        self.assertEqual(response.data.get('qy'), qy, response.data)
        self.assertEqual(response.data.get('price'),
                         self.product.price * qy, response.data)
        self.assertEqual(response.data.get('product'),
                         self.product.id, response.data)
        self.assertEqual(response.data.get('shop'),
                         self.product.shop.id, response.data)
        self.assertEqual(self.product.stock_pcs,
                         before_stock_pcs - qy, response.data)

    @skip('not implement sign in mechanism yet')
    def test_vip_user_can_buy_vip_product(self):
        pass

    def test_delete_order(self):
        order_id = self.order.id
        product = self.order.product
        before_stock_pcs = product.stock_pcs

        response = self.client.delete(
            '/api/order/{}/'.format(order_id),
        )

        product.refresh_from_db()

        self.assertEqual(len(Order.objects.filter(id=order_id)),
                         0, response.data)
        self.assertEqual(response.data.get('before_amount'),
                         before_stock_pcs, response.data)
        self.assertEqual(response.data.get('after_amount'),
                         product.stock_pcs, response.data)
