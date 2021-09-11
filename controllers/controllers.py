# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import route, request


class Controllers(http.Controller):
    @route('/hello_world/delivery_carrier/save_data_send_shipping', auth='user', type='json', methods=['POST'])
    def save_data_send_shipping(self):
        user = request.env['res.users'].browse([request.uid])
        stock_picking_id = request.params.get('stock_picking_id')
        tracking_number = request.params.get('tracking_number')
        label_data = request.params.get('label_data')
        
        # Check that the user is in the group
        if not user.has_group('stock.group_stock_user'):
            return {'error_message': 'Error. You don\'t have permissions in the stock'}
        elif not stock_picking_id or not tracking_number or not label_data:
            return {'error_message': 'Error. Missing parameters (stock_picking_id, tracking_number, label_data)'}
        
        stock_picking = request.env['stock.picking'].browse([stock_picking_id])
        stock_picking.write({
            'tracking_number_response': tracking_number,
            'label_data_response': label_data
        })

        return {'error_message': False}
