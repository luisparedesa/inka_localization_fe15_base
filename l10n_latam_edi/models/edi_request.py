# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime, date, timedelta
import json, requests
import urllib3
from odoo.exceptions import UserError, RedirectWarning

class EdiEcRequest(models.Model):
    _name = 'l10n_edi.request'
    _description = 'EDI EC Request'

    partner_id = fields.Many2one('res.partner', 'Partner', default=lambda self: self.partner_id)
    document_number = fields.Char(string='Document number')
    model = fields.Char(string='Model Name')
    res_id = fields.Integer(string='Record ID', help="ID of the target record in the database")
    type = fields.Selection([('invoice','Invoice')], string='Document ype')
    document_date = fields.Date(string='Document date')
    reference = fields.Char(string='Reference', compute='_compute_reference', readonly=True, store=False)
    log_ids = fields.One2many('l10n_pe_edi.request.log','request_id', string='EDI log', copy=False)

    @api.depends('model', 'res_id')
    def _compute_reference(self):
        for res in self:
            res.model
            res.reference = "%s,%s" % (res.model, res.res_id)

    def action_document_send(self):
        for doc in self:
            model = doc.model
            res_id = doc.res_id
            if model and res_id:
                self.env[model].browse(res_id).action_document_send()

    def action_open_edi_request(self):

        self.ensure_one()
        model = self.model
        res_id = self.res_id
        if model and res_id:
            self.env[model].browse(res_id).action_document_send()
            return {
                'name': _('EDI Request'),
                'view_mode': 'form',
                'res_model': 'l10n_edi.request',
                'res_id': self.id,
                'type': 'ir.actions.act_window',
            }
        return True


class L10nPeEdiRequestLog(models.Model):
    _name = 'l10n_pe_edi.request.log'
    _description = 'Log response'
    _order = 'date desc'

    date = fields.Datetime('Date', default=fields.Datetime.now, required=True)
    json_sent = fields.Html('JSON sent')
    json_response = fields.Html('JSON response')
    request_id = fields.Many2one('l10n_pe_edi.request', string='EDI request')
