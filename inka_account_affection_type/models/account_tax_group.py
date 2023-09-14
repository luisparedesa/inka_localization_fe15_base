# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountTaxAffectionType(models.Model):
    _inherit = "account.tax.group"

    affection_id = fields.Many2one(
        'inka.account.affection.type',
        string=u'T. Afectación',
    )




