# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    # l10n_edi_request_id = fields.Text(
    #     string=u"Json Generado"
    # )

    l10n_edi_request_id = fields.Many2one('l10n_edi.request', string='request')

    def action_document_send(self):

        if not self.journal_id.is_electronic_invoice:
            raise UserError(_('The invoice is not a Electronic document'))
        for move in self:

            # if not move.l10n_edi_request_id:
            l10n_edi_request_id = {
                'partner_id': move.partner_id.id,
                'name': move.partner_id.name,
                'document_number': move.name,
                'document_date': move.invoice_date,

                # 'invoice_line_ids':[
                #     {
                #         'product_id': move.invoice_line_ids.product_id,
                #         'Price_unit': move.invoice_line_ids.price_unit,
                #     }
                # ]
            }
            move.write({'l10n_edi_request_id': l10n_edi_request_id})

    def action_open_edi_request(self):
        self.ensure_one()
        a = self.l10n_edi_request_id
        b=a
        if not self.l10n_edi_request_id:
            return {
                'name': _('EDI Request'),
                'view_mode': 'form',
                'res_model': 'l10n_edi.request',
                'res_id': self.l10n_edi_request_id.id,
                'type': 'ir.actions.act_window',
            }
        return True