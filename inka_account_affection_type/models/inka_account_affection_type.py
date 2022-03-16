# -*- coding: utf-8 -*-
from odoo import api, fields, models

class AffectionTypeBase(models.Model):
    _name = 'inka.account.affection.type'
    _description = 'Affection Type'

    code = fields.Char(required=True, translate=True)
    name = fields.Char(required=True, translate=True)
    is_visible = fields.Boolean()


