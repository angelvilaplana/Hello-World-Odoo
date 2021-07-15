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
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/web_asset_backend_template.xml',
        'views/views.xml',
        'views/demo_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
