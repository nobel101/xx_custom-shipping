# -*- coding: utf-8 -*-
{
    'name': "xx_custom-shipping",

    'summary': """
        this module add a selection field to the add shipping to the SO """,

    'description': """
        Long description of module's purpose
    """,

    'author': "TechScopeCo",
    'website': "http://www.TechScopeCo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_stock','delivery'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
}
