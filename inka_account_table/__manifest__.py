# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Tablas de Factura Electrónica',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """
 Agrega Tablas de factura electrónica
    """,
    'author': 'Inkaopen Team',
    'support': 'ayudaodoo@gmail.com',
    'depends': ['base',
                'account',
                'inka_account_base',
                ],
    'data': [
        'views/inka_account_table_document_type_views.xml',
        'security/ir.model.access.csv',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}

