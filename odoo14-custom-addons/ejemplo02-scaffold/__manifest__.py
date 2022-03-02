# -*- coding: utf-8 -*-
{
    'name': "Ejemplo02-scaffold",

    'summary': """
        ArteMad's summary""",

    'description': """
        Modulo de odoo creado por entusiastas de la artesania.
    """,

    'author': "arteMAD",
    'website': "https://github.com/manu0120",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
