# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, api


class PatientMedicalTag(models.Model):
    _name = 'patient.medical.tag'
    _description = 'Patient Medical Tag'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
