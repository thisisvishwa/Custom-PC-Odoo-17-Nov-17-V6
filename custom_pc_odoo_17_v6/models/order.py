```python
from odoo import models, fields, api

class Order(models.Model):
    _name = 'custom_pc_odoo_17_v6.order'
    _description = 'Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: ('New'))
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('sale', 'Sale Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    date_order = fields.Datetime(string='Order Date', required=True, readonly=True, index=True, copy=False, default=fields.Datetime.now)
    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True, required=True, change_default=True, index=True, tracking=1, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]})
    order_line = fields.One2many('custom_pc_odoo_17_v6.order.line', 'order_id', string='Order Lines', states={'cancel': [('readonly', True)], 'done': [('readonly', True)]}, copy=True, auto_join=True)
    amount_total = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all', tracking=5)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('custom_pc_odoo_17_v6.order') or '/'
        return super(Order, self).create(vals)

    @api.depends('order_line.price_total')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': order.pricelist_id.currency_id.round(amount_untaxed),
                'amount_tax': order.pricelist_id.currency_id.round(amount_tax),
                'amount_total': amount_untaxed + amount_tax,
            })

class OrderLine(models.Model):
    _name = 'custom_pc_odoo_17_v6.order.line'
    _description = 'Order Line'

    order_id = fields.Many2one('custom_pc_odoo_17_v6.order', string='Order Reference', required=True, ondelete='cascade', index=True, copy=False)
    product_id = fields.Many2one('product.product', string='Product', domain=[('sale_ok', '=', True)], change_default=True, ondelete='restrict', check_company=True)
    product_uom_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=True, default=1.0)
    price_unit = fields.Float('Unit Price', required=True, digits='Product Price', default=0.0)
    price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', readonly=True, store=True)
    price_total = fields.Monetary(compute='_compute_amount', string='Total', readonly=True, store=True)

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })
```