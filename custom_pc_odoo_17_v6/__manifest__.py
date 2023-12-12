{
    'name': 'custom_pc_odoo_17_v6',
    'version': '1.0',
    'category': 'Website/Website Themes',
    'summary': 'Advanced eCommerce Website Theme for Custom PC Building',
    'sequence': 1,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'website_sale', 'website_forum', 'stock', 'sale_management', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/pc_builder_view.xml',
        'views/product_view.xml',
        'views/pricing_view.xml',
        'views/review_view.xml',
        'views/order_view.xml',
        'data/product_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
    This module provides a sophisticated, feature-rich eCommerce theme for gaming products in Odoo 17 CE. 
    It emphasizes a robust, user-friendly platform for custom PC building, product sales, and customer engagement.
    """
}