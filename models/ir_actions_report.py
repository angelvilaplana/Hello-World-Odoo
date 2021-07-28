# -*- coding: utf-8 -*-

from odoo import models
from odoo.exceptions import ValidationError

class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def render_template(self, template, values=None):
        report = super(IrActionsReport, self).render_template(template, values)
        if template == 'stock.report_picking':
            raise ValidationError(type(11))
        return report
