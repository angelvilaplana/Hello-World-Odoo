# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    claims_ids = fields.Many2many('crm.claim', 'id', string='Claims')
