```python
from odoo import models, fields, api

class Review(models.Model):
    _name = 'custom_pc_odoo_17_v6.review'
    _description = 'Review'

    product_id = fields.Many2one('custom_pc_odoo_17_v6.product', string='Product', required=True)
    user_id = fields.Many2one('res.users', string='User', required=True)
    rating = fields.Selection([(num, str(num)) for num in range(1, 6)], string='Rating', required=True)
    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description', required=True)
    performance = fields.Selection([(num, str(num)) for num in range(1, 6)], string='Performance')
    durability = fields.Selection([(num, str(num)) for num in range(1, 6)], string='Durability')
    value = fields.Selection([(num, str(num)) for num in range(1, 6)], string='Value')

    @api.model
    def submit_review(self, product_id, user_id, rating, title, description, performance, durability, value):
        review = self.create({
            'product_id': product_id,
            'user_id': user_id,
            'rating': rating,
            'title': title,
            'description': description,
            'performance': performance,
            'durability': durability,
            'value': value
        })
        return review.id
```