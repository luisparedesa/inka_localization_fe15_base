# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'EDI extends base',
    'version': '1.0',
    'category': 'account',
    'description': """
 Extend EDI model
    """,
    'depends': ['base',
                'account',
                'account_edi',
                ],
    'data': [
        'views/account_edi_document.xml',
        'views/edi_request_view.xml'
    ],
    'auto_install': True,
    'license': 'LGPL-3',
}
