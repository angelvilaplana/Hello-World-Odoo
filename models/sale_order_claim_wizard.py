# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrderClaimWizard(models.Model):
    _name = "hello_world.sale_order_claim_wizard"
    _description = "Sale Order Claim Wizard"

    sale_id = fields.Many2one('sale.order', 'Sale Order')
    claims_sales = fields.Many2many(related="sale_id.claims_ids", string='Claims')

    def get_message(self, sale_id, name='Sale Order Claims'):
        partial_id = self.search([('sale_id', '=', sale_id)], limit=1).id

        if not partial_id:
            partial_id = self.create({'sale_id': sale_id}).id

        return {
            'name':name,
            'view_mode': 'form',
            'view_id': False,
            'res_model': 'hello_world.sale_order_claim_wizard',
            'res_id': partial_id,
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'new',
            'domain': '[]',
        }
