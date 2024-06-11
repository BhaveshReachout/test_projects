# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, Command, fields, models


class PropertyProperty(models.Model):
    _name = 'property.property'
    _description = 'Property'
    _order = "id desc"

    name = fields.Char('Property Name', required=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Date Availability')
    expected_price = fields.Float('Expected Price')
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('Bedrooms')
    living_area = fields.Integer('living_area')
    facades = fields.Integer('facades')
    garage = fields.Boolean('garage')
    garden = fields.Boolean('garden')
    garden_area = fields.Integer('garden_area')
    garden_orientation = fields.Selection(string='garden_orientation', selection=[(
        'north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West'),], default='north',)
        
    def action_sold(self):
        a = 10/0
