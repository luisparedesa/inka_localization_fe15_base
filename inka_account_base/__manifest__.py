# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Base de Factura Electrónica',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """
 Base de Factura Electrónica
    """,
    'author': 'Inkaopen Team',
    'support': 'ayudaodoo@gmail.com',
    'depends': ['base',
                'account',
                'l10n_latam_base',
                ],
    'data': [
        'views/inka_account_base_views.xml',
        'views/inka_account_identification_type_views.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}

