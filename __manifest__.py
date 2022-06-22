# -*- coding: utf-8 -*-
{
    'name': "modulo_prueba",

    'summary': """
        Emanuel Esquivel L. Module 001""",

    'description': """
        Prueba tecnica Grupo O-LA
    """,

    'author': "Emanuel Esquivel L.",
    'website': "https://github.com/ema11412",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'sequence': -100,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
    'application': True,

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
