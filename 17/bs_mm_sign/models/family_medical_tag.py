# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, api


class FamilyMedicalTag(models.Model):
    _name = 'family.medical.tag'
    _description = 'Family Medical Tag'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
