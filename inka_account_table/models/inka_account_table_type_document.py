# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AccountTableTypeDocument(models.Model):
    _name = 'inka.account.table.type.document'
    _description = 'Type document'

    code_at = fields.Char(string="Código",required=True, translate=True)
    name = fields.Char(string="Nombre",required=True, translate=True)
    code_table = fields.Char(string="Código de Tabla",required=True, translate=True)
    is_visible = fields.Boolean(string="Visible")


