
# -*- encoding: utf-8 -*-
{
    'name': 'Form Customization',
    'version': '11.0.1.0.2',
    'category': 'Customization',
    'summary': 'Form Customization',
    'description': "Form Customization",
    'author': "Knowledge Bases",
    'website': "https://www.knowledge-bases.com",
    'company': 'Knowledge Bases',
    'depends': ['account_invoicing', 'stock', 'sale_management'],
    'data': [
            'views/form_customization.xml',
            'wizard/stock_change_product_qty_view.xml',
    ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
