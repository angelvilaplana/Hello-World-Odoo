# -*- coding: utf-8 -*-

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    tracking_number_response = fields.Text(
        string="Last SEUR xml request",
        help="Used to prevent duplicate api calls",
        copy=False,
        readonly=True,
    )

    label_data_response = fields.Text(
        string="Last label data response",
        help="Used to prevent duplicate api calls",
        copy=False,
        readonly=True,
    )
