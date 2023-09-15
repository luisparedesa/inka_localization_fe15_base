# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountMoveAffectionType(models.Model):
    _inherit = "account.move.line"

    affection_id = fields.Many2one(
        'inka.account.affection.type',
        string=u"T. Afectación",
    )

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            tax_group = self.product_id.taxes_id and self.product_id.taxes_id[0].tax_group_id
            if tax_group:
                affection = self.env['inka.account.affection.type'].search(
                    [('code_at', '=', tax_group.affection_id.code_at)], limit=1)
                if affection:
                    self.affection_id = affection.id
