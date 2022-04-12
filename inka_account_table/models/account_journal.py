# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountTableJournal(models.Model):
    _inherit = "account.journal"

    document_type_id = fields.Many2one(
        'inka.account.table.document.type',
        string=u'Tipo de documento',
    )






