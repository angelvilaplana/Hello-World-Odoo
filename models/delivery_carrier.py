# -*- coding: utf-8 -*-

from odoo import fields, models, http
from odoo.exceptions import ValidationError
import json
import requests


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(
        selection_add=[("hello_world", "Hello World")]
    )

    def hello_world_send_shipping(self, pickings):
        res = []
        for picking in pickings:
            # If you have tracking_number and label_data,
            # is not necessary to "call API" again
            carrier_tracking = self.env['hello_world.carrier_tracking'].search(
                [('stock_picking_id','=',picking.id)], limit=1)
            if carrier_tracking and carrier_tracking.tracking_number and carrier_tracking.label_data:
                self.picking_message_post(
                    picking, 
                    carrier_tracking.tracking_number, 
                    carrier_tracking.label_data
                )
                res.append({
                    'exact_price': 0.0,
                    'tracking_number': carrier_tracking.tracking_number
                })
            else:
                # Simulate call api & get values
                tracking_number = 'XXXXXXXX'
                label_data = 'Hello World Label Data Content Test'

                # Save data in the "carrier_tracking" table by calling a controller
                self.picking_save_data(picking, tracking_number, label_data)

                # Post message Picking with the label data
                self.picking_message_post(picking, tracking_number, label_data)

                # Simulate an  error out of nowhere
                raise ValidationError('Hello World, Error to simulate an error')

                # Add the data in the array to return
                res.append({
                    'exact_price': 0.0,
                    'tracking_number': tracking_number
                })
        return res

    def picking_save_data(self, picking, tracking_number, label_data):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        save_picking_data_url = base_url + '/hello_world/delivery_carrier/save_data_send_shipping'
                
        response = requests.post(
            save_picking_data_url, 
            data=json.dumps({
                'params': {
                    'stock_picking_id': picking.id,
                    'tracking_number': tracking_number,
                    'label_data': label_data
                }
            }), 
            headers={'Content-Type': 'application/json'},
            cookies={'session_id': http.request.session.sid }
        )

        result = response.json().get('result')
        error_message = result.get('error_message')
        if error_message:
            raise ValidationError(error_message)

    def picking_message_post(self, picking, tracking_number, label_data):
        message_body = "Generate Hello World label data file"
        picking.message_post(
            body=message_body, 
            attachments=[
                (
                    'Hello World Label-{}.txt'.format(tracking_number), 
                    label_data
                )
            ]
        )
