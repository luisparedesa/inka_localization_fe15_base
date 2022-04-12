# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AccountAffectionType(models.Model):
    _name = 'inka.account.affection.type'
    _description = 'Affection Type'

    code_at = fields.Char(string=u"Código",required=True, translate=True)
    name = fields.Char(string=u"Nombre",required=True, translate=True)
    is_visible = fields.Boolean(string=u"Visible")





