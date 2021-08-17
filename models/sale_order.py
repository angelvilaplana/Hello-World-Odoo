# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    claims_ids = fields.Many2many('crm.claim', 'id', 
        string='Claims', 
        ondelete="cascade"
    )

    claims_not_rejected = fields.Many2many('crm.claim', 'id',
        compute="_compute_claims_not_rejected",
        store=False
    )


    @api.depends('claims_ids')
    def _compute_claims_not_rejected(self):
        for rec in self:
            rec.claims_not_rejected = rec.claims_ids.filtered_domain([
                ('stage_id.name', '!=', 'Rechazada')
            ])


    def action_show_claims(self):
        return self.env['hello_world.sale_order_claim_wizard'].get_message(self.id)
