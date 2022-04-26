# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class AccountEdiDocument(models.Model):
    _inherit = 'account.edi.document'

    url_document = fields.Char(
        string='URL'
    )



