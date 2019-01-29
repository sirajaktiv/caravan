
# -*- encoding: utf-8 -*-
{
    'name': 'Report Extended',
    'version': '11.0.1.4.0',
    'category': 'Report',
    'summary': 'Report Extended',
    'description': "Invoice Report Extended",
    'author': "Knowledge Bases",
    'website': "https://www.knowledge-bases.com",
    'company': 'Knowledge Bases',
    'depends': ['account', 'form_customization'],
    'data': [
        'report/report_template.xml',
        'views/account_invoice.xml',
        'views/res_company_view.xml'
    ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
