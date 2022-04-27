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
            l10n_edi_request_id = self.env['l10n_edi.request'].create({
                'partner_id': move.partner_id.id,
                'document_number': move.name,
                'model': self._name,
                'res_id': self.id,
                'type': 'invoice',
                'document_date': move.invoice_date})
            move.write({'l10n_edi_request_id': l10n_edi_request_id})

    def action_open_edi_request(self):
        self.ensure_one()
        if self.l10n_edi_request_id:
            return {
                'name': _('EDI Request'),
                'view_mode': 'form',
                'res_model': 'l10n_edi.request',
                'res_id': self.l10n_edi_request_id.id,
                'type': 'ir.actions.act_window',
            }
        return True