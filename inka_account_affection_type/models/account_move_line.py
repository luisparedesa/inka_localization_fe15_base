# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountMoveAffectionType(models.Model):
    _inherit = "account.move.line"

    affection_id = fields.Many2one(
        'inka.account.affection.type',
        string='Tipo de Afectación',
    )




