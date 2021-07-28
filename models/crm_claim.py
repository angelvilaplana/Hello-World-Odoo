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
                sale_order = self.env['sale.order'].search([('id', '=', model_value_id)])
                claims = sale_order.claims_ids
                sale_order.write({'claims_ids': claims + claim})
        return claim

    def write(self, vals):
        res = super(CrmClaim, self).write(vals)
        return res
        raise Exception('Write')

    def unlink(self):
        res = super(CrmClaim, self).unlink()
        return res
        raise Exception('Unlink')
