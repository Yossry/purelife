# -*- coding: utf-8 -*-
from datetime import datetime
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class bt_mrp_workcenter(models.Model): 
    _inherit = "mrp.workcenter"

    user_view_ids = fields.Many2many('res.users', string='Usuarios')

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        return super(bt_mrp_workcenter, self).fields_view_get(view_id, view_type, toolbar, submenu)

    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        
        if self.env.user.has_group('bt_mrp_ao_1.group_bt_mrp_workcenter_ao_1'):
            res = self.env["mrp.workcenter"].search([('user_view_ids','in',self.env.user.id)])
            if len(res):  
                domain.append(('id','in',res.ids))  

        return super(bt_mrp_workcenter, self).search_read(domain, fields, offset, limit, order)

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):    
        return super(bt_mrp_workcenter, self).search(args, offset=0, limit=None, order=None, count=False)

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        
        # res = self.env["mrp.workcenter"].search([('user_view_ids','in',self.env.user.id)])
        # if len(res):
        #     pass

        # default_code = self.get_search_default_code(args)
        # print(args)
        # print("default_code => %s" % default_code)
        # if default_code:
        #     ids_equivalence = self.env["bt.product.equivalence"].search([('code_oem','=',default_code)])
        #     new_args = self.struct_search('code_equivalence', [x.code_equivalence for x in ids_equivalence])
        #     print(new_args)
        #     if len(new_args):
        #         ids_equivalence = self.env["bt.product.equivalence"].search(new_args)   
        #         new_args = self.struct_search('default_code', [x.code_oem for x in ids_equivalence])
        #         print(new_args)

        #         # new_args.append(('default_code','=',default_code))

        #         condition = []
        #         i=0
        #         while i < (len(new_args)):
        #             condition.append('|')
        #             i+=1
        #         print(condition)
        #         # ids_equivalence_args = [x.code_oem for x ]
        #         # new_args = default_code

        #         args = condition + new_args + args
        #         print(args)
        res = super(bt_mrp_workcenter, self)._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)
        return res

    # def struct_search(self, name_filter, args):
    #     new_args = [(name_filter,'=',x) for x in args]
    #     return new_args

    # def get_search_default_code(self, args):
    #     default_code = False
    #     for x in args:
    #         if x[0] == 'default_code':
    #             default_code = x[2]
    #     return default_code