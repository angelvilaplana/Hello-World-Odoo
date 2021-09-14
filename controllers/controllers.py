# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import route, request


class Controllers(http.Controller):
    @route('/hello_world/delivery_carrier/save_data_send_shipping', auth='user', type='json', methods=['POST'])
    def save_data_send_shipping(self, **kwargs):
        user = request.env['res.users'].browse([request.uid])
        stock_picking_id = kwargs.get('stock_picking_id')
        tracking_number = kwargs.get('tracking_number')
        label_data = kwargs.get('label_data')
        
        # Check that the user is in the group
        if not user.has_group('stock.group_stock_user'):
            return {'error_message': 'Error. You don\'t have permissions in the stock'}
        elif not stock_picking_id or not tracking_number or not label_data:
            return {'error_message': 'Error. Missing parameters (stock_picking_id, tracking_number, label_data)'}
        
        # Save expedition data in the "carrier_tracking" table
        request.env['hello_world.carrier_tracking'].create({
            'stock_picking_id': stock_picking_id,
            'tracking_number': tracking_number,
            'label_data': label_data
        })

        return {'error_message': False}
