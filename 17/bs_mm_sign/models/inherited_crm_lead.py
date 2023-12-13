# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, api, _


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    medical_history_count = fields.Integer(related='partner_id.medical_history_count')
    toggle = fields.Boolean(default=False)
    is_intake_complete = fields.Boolean(default=False)
    new_opportunity_date = fields.Datetime()
    is_so_complete = fields.Boolean(default=False)
    collect_lab_info_date = fields.Datetime()

    # @api.model
    # def create(self, values):
    #     if 'stage_id' in values and isinstance(values.get('stage_id'), int):
    #         stage_id = self.env['crm.stage'].browse(values.get('stage_id'))
    #         if not stage_id:
    #             raise ValueError('State is not found.')
    #         if stage_id.name == 'New Opportunity':
    #             values['new_opportunity_date'] = fields.Datetime.now()
    #         elif stage_id.name == 'Collect Lab Info':
    #             values['collect_lab_info_date'] = fields.Datetime.now()
    #         elif stage_id.name == 'Labs':
    #             pass
    #         elif stage_id.name == 'NP Consult':
    #             pass
    #         elif stage_id.name == 'Order Products':
    #             pass
    #     return super(CRMLead, self).create(values)
    #
    # def write(self, values):
    #     if 'stage_id' in values and isinstance(values.get('stage_id'), int):
    #         stage_id = self.env['crm.stage'].browse(values.get('stage_id'))
    #         if not stage_id:
    #             raise ValueError('State is not found.')
    #         if stage_id.name == 'New Opportunity':
    #             values['new_opportunity_date'] = fields.Datetime.now()
    #         elif stage_id.name == 'Collect Lab Info':
    #             values['collect_lab_info_date'] = fields.Datetime.now()
    #     return super(CRMLead, self).write(values)

    # @api.onchange('is_intake_complete')
    # def onchange_is_intake_complete(self):
    #     if self.is_intake_complete:
    #         self.intake_date = fields.Datetime.now()
    #
    # @api.onchange('is_so_complete')
    # def onchange_is_so_complete(self):
    #     if self.is_so_complete:
    #         self.so_confirm_date = fields.Datetime.now()

    def action_view_medical_history(self):
        if self.partner_id.medical_history_ids:
            return {
                'type': 'ir.actions.act_window',
                'target': 'current',
                'name': _('Medical History'),
                'view_mode': 'tree,form',
                'res_model': 'medical.history',
                'domain': [('id', 'in', self.partner_id.medical_history_ids.ids)],
            }

    def change_toggle(self):
        self.toggle = not self.toggle
