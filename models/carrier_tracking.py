# -*- coding: utf-8 -*-

from odoo import fields, models

class CarrierTracking(models.Model):
    _name = "hello_world.carrier_tracking"

    stock_picking_id = fields.Many2one('stock.picking', 'Stock Picking')

    tracking_number = fields.Char(
        string="Last tracking number response",
        help="Used to prevent duplicate api calls",
        copy=False,
        readonly=True,
    )

    label_data = fields.Text(
        string="Last label data response",
        help="Used to prevent duplicate api calls",
        copy=False,
        readonly=True,
    )
