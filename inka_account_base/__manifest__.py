# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Base de Factura ',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """
 Mostrar campos que no se ven en el estándar
    """,
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

