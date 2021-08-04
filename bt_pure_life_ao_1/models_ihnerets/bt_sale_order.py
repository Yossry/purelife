# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class bt_sale_order(models.Model):  
    _inherit = "sale.order"

    name_patient = fields.Char(string='Nombre del paciente')
     
    pla_service = fields.Char(string='PLA Service')

    @api.model
    def default_get(self, fields):
        res = super(bt_sale_order, self).default_get(fields)
        return res