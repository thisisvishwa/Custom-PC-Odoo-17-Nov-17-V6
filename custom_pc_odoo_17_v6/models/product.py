```python
from odoo import models, fields, api

class Product(models.Model):
    _name = 'custom_pc_odoo_17_v6.product'
    _description = 'Product Model for Custom PC Builder'

    name = fields.Char(string='Product Name', required=True)
    product_type = fields.Selection([
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('motherboard', 'Motherboard'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('power_supply', 'Power Supply'),
        ('cooling_solution', 'Cooling Solution'),
        ('case', 'Case'),
        ('prebuilt_pc', 'Prebuilt PC'),
        ('laptop', 'Laptop'),
        ('console', 'Console'),
        ('accessory', 'Accessory'),
    ], string='Product Type', required=True)
    image = fields.Binary(string='Product Image')
    image_360 = fields.Binary(string='360 Degree View')
    specifications = fields.Text(string='Specifications')
    user_manual = fields.Binary(string='User Manual')
    installation_guide = fields.Binary(string='Installation Guide')
    stock_level = fields.Integer(string='Stock Level')
    reorder_alert = fields.Boolean(string='Reorder Alert', compute='_compute_reorder_alert')

    @api.depends('stock_level')
    def _compute_reorder_alert(self):
        for record in self:
            if record.stock_level < 10:
                record.reorder_alert = True
            else:
                record.reorder_alert = False
```