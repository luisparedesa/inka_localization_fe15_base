# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Tipos de Afectación',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """
 Agrega mantenimiento de tipos de afectación
    """,
    'depends': ['base',
                'account',
                'inka_account_base',
                ],
    'data': [
        'views/inka_account_affection_type_views.xml',
        'security/ir.model.access.csv',
        #Honduras
        'data/affection_type_hn_data.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}

