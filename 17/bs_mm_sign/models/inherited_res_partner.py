# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    medical_history_ids = fields.One2many('medical.history', 'partner_id')
    medical_history_count = fields.Integer(compute='compute_medical_history_count')
    best_phone = fields.Char(string='Best Contact Phone Number')
    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed')
    ], string='Marital Status')
    emergency_name = fields.Char(string='Emergency Contact Name')
    relationship = fields.Char(string='Relationship')
    emergency_number = fields.Char(string='Emergency Contact Number')
    office_can_msg = fields.Boolean(string='Office may leave messages on answering machine')
    office_can_call = fields.Boolean(string='Office may call cell phone')
    office_can_call_at_work = fields.Boolean(string='Office may call patient at work')
    office_can_msg_spouse = fields.Boolean(string='Office may leave message with spouse and/or significant other.')
    office_only_speak = fields.Boolean(string='Office should only speak with patient.')
    family_member_info = fields.Char(string='Information may be given to other family members. List')

    patient_med_tag_ids = fields.Many2many('patient.medical.tag', 'partner_patient_med_history_tag_rel', string="Patient Medical History")
    family_med_tag_ids = fields.Many2many('family.medical.tag', 'partner_family_med_history_tag_rel', string="Family Medical History")

    @api.depends('medical_history_ids')
    def compute_medical_history_count(self):
        for rec in self:
            rec.medical_history_count = len(rec.medical_history_ids.ids) if rec.medical_history_ids else 0

    def action_view_medical_history(self):
        if self.medical_history_ids:
            return {
                'type': 'ir.actions.act_window',
                'target': 'current',
                'name': _('Medical History'),
                'view_mode': 'tree,form',
                'res_model': 'medical.history',
                'domain': [('id', 'in', self.medical_history_ids.ids)],
            }
