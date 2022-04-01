# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountTableJournal(models.Model):
    _inherit = "account.journal"

    document_type_id = fields.Many2one(
        'inka.account.table.type.document',
        string='Tipo de documento',
    )

    move_cai = fields.Char(
        string="C.A.I.",
        required=False,
        translate=True
    )




