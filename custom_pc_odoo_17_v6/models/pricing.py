```python
from odoo import models, fields, api

class Pricing(models.Model):
    _name = 'custom_pc_odoo_17_v6.pricing'
    _description = 'Pricing Model'

    product_id = fields.Many2one('custom_pc_odoo_17_v6.product', string='Product')
    price = fields.Float(string='Price')
    discount = fields.Float(string='Discount')
    bundle_offer_id = fields.Many2one('custom_pc_odoo_17_v6.bundle_offer', string='Bundle Offer')

    @api.model
    def calculate_price(self, product_id, quantity):
        product = self.env['custom_pc_odoo_17_v6.product'].browse(product_id)
        price = product.price * quantity
        return price

    @api.model
    def apply_discount(self, product_id, discount_code):
        discount = self.env['custom_pc_odoo_17_v6.discount'].search([('code', '=', discount_code)])
        if discount:
            product = self.env['custom_pc_odoo_17_v6.product'].browse(product_id)
            discounted_price = product.price - (product.price * (discount.rate / 100))
            return discounted_price
        else:
            return False

    @api.model
    def get_bundle_offer(self, product_ids):
        bundle_offer = self.env['custom_pc_odoo_17_v6.bundle_offer'].search([('product_ids', 'in', product_ids)])
        if bundle_offer:
            return bundle_offer
        else:
            return False
```