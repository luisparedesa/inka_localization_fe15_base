# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Tablas de Factura Electrónica',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """
 Tablas de factura electrónica
    """,
    'depends': ['base',
                'account',
                'inka_account_base',
                ],
    'data': [
        'views/inka_account_table_type_document_views.xml',
        'security/ir.model.access.csv',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}

