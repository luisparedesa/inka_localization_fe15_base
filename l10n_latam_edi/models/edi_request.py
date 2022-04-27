# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime, date, timedelta
import json, requests
import urllib3
from odoo.exceptions import UserError, RedirectWarning

class EdiEcRequest(models.Model):
    _name = 'l10n_edi.request'
    _description = 'EDI EC Request'


    name = fields.Char(string='Description', size=128, index=True, required=True, default='New')
    partner_id = fields.Many2one('res.partner', 'Partner', default=lambda self: self.partner_id)
    document_type = fields.Many2one('inka.account.table.document.type', 'Document_Type')
    document_number = fields.Char(string='Document number')
    model = fields.Char(string='Model Name')
    res_id = fields.Integer(string='Record ID', help="ID of the target record in the database")
    type = fields.Selection([('invoice','Invoice')], string='Document ype')
    document_date = fields.Date(string='Document date')
    reference = fields.Char(string='Reference', compute='_compute_reference', readonly=True, store=False)

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