# -*- coding: utf-8 -*-
{
    'name': 'odoo framework',
    'version': '17.0.1.0',
    'website': '',
    'category': 'Sales',
    'summary': '',
    'description': """ """,
    'depends': [],
    'data': [
          'security/ir.model.access.csv',
          'views/property_property_views.xml',
         ],
    'demo': [],
    'installable': True,
    'assets': {
        'web.assets_backend': [
            'odoo_framework_v17/static/src/js/my_test_field.js',
        ],
        'web.assets_frontend': [
        ],
        'web.report_assets_common': [
        ],
        'web.report_assets_pdf': [
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
