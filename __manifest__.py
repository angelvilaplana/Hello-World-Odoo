# -*- coding: utf-8 -*-
{
    'name': "Hello World",

    'summary': """
        Addon to do proves
    """,

    'description': """
        Addon to do proves
    """,

    'author': "Angel Vil",
    'website': "https://github.com/angelvilaplana",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'crm', 'sale'],

    # always loaded
    'data': [
        'security/hello_world_security.xml',
        'security/ir.model.access.csv',
        'views/web_asset_backend_template.xml',
        'views/sale_order_claim_wizard.xml',
        'views/views.xml',
        'views/sale_order.xml',
        'views/demo_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
