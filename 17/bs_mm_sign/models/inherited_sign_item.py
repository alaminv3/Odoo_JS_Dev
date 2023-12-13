# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (https://www.bistasolutions.com)
#
##############################################################################

import base64
from datetime import datetime
from dateutil import parser
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError, AccessError
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT


def parse_date_value(value):
    # Attempt to create a datetime object from the input value.
    try:
        date_obj = parser.parse(value, dayfirst=False, yearfirst=False)
        return date_obj
    except ValueError:
        return False
    except OverflowError:
        return False


class InheritedSignRequest(models.Model):
    _inherit = 'sign.request'

    def write(self, vals):
        if 'state' in vals and vals.get('state', False) == 'signed':
            sign_request_items = self.request_item_ids.filtered(lambda item: item.state == 'completed')
            for sign_request_item in sign_request_items:
                data_model = {}
                related_partner = sign_request_item.partner_id
                item_values = sign_request_item.sign_item_value_ids
                for item_value in item_values.filtered(lambda item: item.model_id and item.field_id):
                    model_name = item_value.model_id.model
                    field_name = item_value.field_id.name
                    field_type = item_value.field_id.ttype
                    field_action = item_value.field_action
                    value = item_value.value
                    sign_field_type = item_value.sign_item_id.type_id.item_type
                    model_obj = None

                    # Check if the value is str or not. all data from sign doc is str
                    if not isinstance(value, str):
                        continue

                    if sign_field_type in ['signature', 'initial']:
                        byte_data = value.split('base64,')[1]
                        value = byte_data
                    elif sign_field_type == 'checkbox':
                        value = True if value == 'on' else False
                    elif sign_field_type == 'selection':
                        option = None
                        try:
                            option_id = int(value)
                            option = self.env['sign.item.option'].browse(option_id)
                        except:
                            continue
                        value = option.key if option and option.key else False
                    elif sign_field_type in ['text', 'textarea']:
                        # If field_type is from str fields, then check separately. Try to convert first to it's actual type.
                        if field_type in ['float', 'integer', 'monetary']:
                            try:
                                value = int(value) if field_type == 'integer' else float(value)
                            except:
                                continue
                            # Check if the field is relational and corresponding value exist or not
                        elif field_type == 'many2one':
                            model_of_field = item_value.field_id.relation
                            domain = [('name', '=', value)] if field_action == 'exact_match' else [
                                ('name', 'ilike', value)]
                            model_obj = self.env[model_of_field].search(domain, limit=1)
                            if not model_obj:
                                continue

                        # If a field is date/datetime, then try to convert it to a date/datetime, if it fails, then value is not correct.
                        elif field_type in ['date', 'datetime']:
                            value = parse_date_value(value)
                            if not value:
                                continue

                    if model_name in data_model.keys():
                        data_model[model_name][
                            field_name] = model_obj.id if field_type == 'many2one' and model_obj else value
                    else:
                        data_model[model_name] = {
                            field_name: model_obj.id if field_type == 'many2one' and model_obj else value
                        }
                # print(data_model)
                try:
                    if data_model:
                        if related_partner and 'res.partner' in data_model.keys():
                            related_partner.sudo().write(data_model['res.partner'])
                        for model in data_model.keys():
                            # TODO: Here we need add some validations like if all required fields value are available or not
                            if model != 'res.partner':
                                new_model_obj = self.env[model].sudo().create(data_model[model])

                # These Exceptions should be removed in order to give a smooth experience to the end user. But For now it's for checking purpose
                except AccessError:
                    raise ValidationError('This user is not allowed to modify the specified records/fields.')
                except ValidationError:
                    raise ValidationError('There are some invalid values for one or more fields.')
                except ValueError:
                    raise ValidationError(
                        'There must be a field name specified in the create values that does not exist.')
                except UserError:
                    raise ValidationError(
                        'A loop is created in a hierarchy of objects such as setting an object as its own parent.')

        return super(InheritedSignRequest, self).write(vals)


class InheritedSignItem(models.Model):
    _inherit = 'sign.item'

    model_id = fields.Many2one('ir.model')
    field_id = fields.Many2one('ir.model.fields', domain="[('model_id', '=', model_id)]")
    field_action = fields.Selection([
        ('exact_match', 'Exact Match'),
        ('partial_match', 'Partial Match'),
    ], default='exact_match')


class InheritedSignRequestItemValue(models.Model):
    _inherit = 'sign.request.item.value'

    model_id = fields.Many2one('ir.model', related='sign_item_id.model_id', store=True)
    field_id = fields.Many2one('ir.model.fields', related='sign_item_id.field_id', store=True)
    field_action = fields.Selection([
        ('exact_match', 'Exact Match'),
        ('partial_match', 'Partial Match'),
    ], related='sign_item_id.field_action')


class InheritSignItemOption(models.Model):
    _inherit = 'sign.item.option'

    key = fields.Char()
