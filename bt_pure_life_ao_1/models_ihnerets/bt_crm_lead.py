# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class bt_crm_lead(models.Model):  
    _inherit = ["crm.lead"]

    name_patient = fields.Char(string='Nombre del paciente')
     
    pla_service = fields.Char(string='PLA Service')
    
    # @api.model
    # def action_sale_quotations_new1(self):
    #     if not self.partner_id:
    #         return self.env["ir.actions.actions"]._for_xml_id("sale_crm.crm_quotation_partner_action")
    #     else:
    #         return self.action_new_quotation()
    
    # @api.model
    def action_new_quotation(self):
        res = super(bt_crm_lead, self).action_new_quotation()
        # res = self.action_new_quotation()
        res['context']['default_name_patient'] = self.name_patient
        res['context']['default_pla_service'] = self.pla_service
        return res


    # # @api.multi
    # def write(self, vals):
    #     return super(bt_crm_lead, self).write(vals)