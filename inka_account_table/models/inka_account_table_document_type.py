# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountTableDocumentType(models.Model):
    _name = 'inka.account.table.document.type'
    _description = 'Document Type'

    code_at = fields.Char(string=u"Código", required=True, translate=True)
    name = fields.Char(string="Nombre", required=True, translate=True)
    code_table = fields.Char(string=u"Código de Tabla", required=True, translate=True)
    is_visible = fields.Boolean(string="Visible")
