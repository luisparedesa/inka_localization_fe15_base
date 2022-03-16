# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Tipos de Afectación - Base',
    'version': '1.0',
    'category': 'Accounting/Accounting',
    'description': """
 Agrega mantenimiento de tipos de afectación
    """,
    'depends': ['base',
                'account',
                ],
    'data': [
        'views/account_report.xml',
        'report/custom_invoice_report.xml',
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}

