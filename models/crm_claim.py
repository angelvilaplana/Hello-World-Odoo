# -*- coding: utf-8 -*-

from odoo import api, models

class CrmClaim(models.Model):
    _inherit = "crm.claim"

    @api.model
    def create(self, vals):
        claim = super(CrmClaim, self).create(vals)
        model_ref_id = vals.get('model_ref_id')
        if model_ref_id:
            model_ref_id = vals.get('model_ref_id').split(',')
            model = model_ref_id[0]
            model_value_id = model_ref_id[1]
            if model == 'sale.order':
                self.add_claim_sale_order(claim, model_value_id)
        return claim


    def write(self, vals):
        sale_order = self.model_ref_id
        claim = super(CrmClaim, self).write(vals)
        model_ref_id = vals.get('model_ref_id')
        if model_ref_id:
            model_ref_id = vals.get('model_ref_id').split(',')
            model = model_ref_id[0]
            model_value_id = model_ref_id[1]
            self.remove_claim_sale_order(sale_order)
            if model == 'sale.order':
                self.add_claim_sale_order(self, model_value_id)
        return claim


    def add_claim_sale_order(self, claim, sale_order_id):
        sale_order = self.env['sale.order'].search([('id', '=', sale_order_id)])
        claims = sale_order.claims_ids
        sale_order.write({'claims_ids': claims + claim})


    def remove_claim_sale_order(self, sale_order):
        if sale_order is None or sale_order._name != 'sale.order':
            return
        claims = sale_order.claims_ids
        if self in claims:
            sale_order.write({'claims_ids': [(3, self.id, 0)]})
