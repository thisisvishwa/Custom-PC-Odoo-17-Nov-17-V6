```python
from odoo.tests import common

class TestOrder(common.TransactionCase):

    def setUp(self):
        super(TestOrder, self).setUp()
        self.Order = self.env['custom_pc_odoo_17_v6.order']

    def test_place_order(self):
        # Create a new order
        new_order = self.Order.create({
            'name': 'Test Order',
            'customer_id': 1,
            'product_ids': [(6, 0, [1, 2, 3])],
            'total_price': 500.00,
            'status': 'pending',
        })

        # Check if the order is created
        self.assertEqual(new_order.name, 'Test Order')
        self.assertEqual(new_order.customer_id, 1)
        self.assertEqual(new_order.total_price, 500.00)
        self.assertEqual(new_order.status, 'pending')

    def test_order_status_change(self):
        # Create a new order
        new_order = self.Order.create({
            'name': 'Test Order',
            'customer_id': 1,
            'product_ids': [(6, 0, [1, 2, 3])],
            'total_price': 500.00,
            'status': 'pending',
        })

        # Change the order status
        new_order.write({'status': 'shipped'})

        # Check if the order status is changed
        self.assertEqual(new_order.status, 'shipped')

    def test_order_total_price_calculation(self):
        # Create a new order
        new_order = self.Order.create({
            'name': 'Test Order',
            'customer_id': 1,
            'product_ids': [(6, 0, [1, 2, 3])],
            'total_price': 500.00,
            'status': 'pending',
        })

        # Calculate the total price
        total_price = new_order.calculate_price()

        # Check if the total price is calculated correctly
        self.assertEqual(total_price, 500.00)
```