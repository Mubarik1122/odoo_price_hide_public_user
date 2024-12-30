# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class price_hide_public_user(models.Model):
#     _name = 'price_hide_public_user.price_hide_public_user'
#     _description = 'price_hide_public_user.price_hide_public_user'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
