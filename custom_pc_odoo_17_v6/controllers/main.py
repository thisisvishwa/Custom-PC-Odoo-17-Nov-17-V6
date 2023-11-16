```python
from odoo import http
from odoo.http import request

class CustomPCController(http.Controller):

    @http.route('/pc_builder', type='http', auth='public', website=True)
    def pc_builder(self, **kwargs):
        return request.render('custom_pc_odoo_17_v6.pc_builder', {})

    @http.route('/products', type='http', auth='public', website=True)
    def products(self, **kwargs):
        products = request.env['custom_pc_odoo_17_v6.product'].search([])
        return request.render('custom_pc_odoo_17_v6.products', {'products': products})

    @http.route('/product/<model("custom_pc_odoo_17_v6.product"):product>', type='http', auth='public', website=True)
    def product(self, product, **kwargs):
        return request.render('custom_pc_odoo_17_v6.product', {'product': product})

    @http.route('/order', type='http', auth='public', website=True)
    def order(self, **kwargs):
        return request.render('custom_pc_odoo_17_v6.order', {})

    @http.route('/review', type='http', auth='public', website=True)
    def review(self, **kwargs):
        return request.render('custom_pc_odoo_17_v6.review', {})

    @http.route('/pricing', type='http', auth='public', website=True)
    def pricing(self, **kwargs):
        return request.render('custom_pc_odoo_17_v6.pricing', {})
```
