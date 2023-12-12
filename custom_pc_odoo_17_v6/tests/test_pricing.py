```python
from odoo.tests import common
from custom_pc_odoo_17_v6.models.pricing import Pricing

class TestPricing(common.TransactionCase):

    def setUp(self):
        super(TestPricing, self).setUp()
        self.Pricing = self.env['pricing']

    def test_calculate_price(self):
        # Create a test product
        product = self.env['product.product'].create({
            'name': 'Test Product',
            'list_price': 1000.0,
            'type': 'product',
        })

        # Create a test pricing
        pricing = self.Pricing.create({
            'product_id': product.id,
            'discount': 10.0,
            'bundle_discount': 5.0,
        })

        # Test the calculate_price method
        price = pricing.calculate_price()
        self.assertEqual(price, 850.0, "The calculated price is not correct")

    def test_bundle_offers(self):
        # Create test products
        product1 = self.env['product.product'].create({
            'name': 'Test Product 1',
            'list_price': 1000.0,
            'type': 'product',
        })
        product2 = self.env['product.product'].create({
            'name': 'Test Product 2',
            'list_price': 500.0,
            'type': 'product',
        })

        # Create a test pricing
        pricing = self.Pricing.create({
            'product_id': product1.id,
            'discount': 10.0,
            'bundle_discount': 5.0,
            'bundle_product_id': product2.id,
        })

        # Test the bundle_offers method
        bundle_price = pricing.bundle_offers()
        self.assertEqual(bundle_price, 1425.0, "The bundle price is not correct")
```