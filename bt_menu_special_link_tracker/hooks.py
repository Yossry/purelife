# Copyright 2021 Nugleo
# # License LGPL-3 or later (http://www.gnu.org/licenses/lgpl).

from os.path import join, dirname, realpath
from odoo.api import Environment, SUPERUSER_ID

ref_menu = 'utm.menu_link_tracker_root'
group_id_new = 'bt_menu_special_link_tracker.group_bt_menu_link_tracker'
groups_ids = ['base.group_no_one']

def post_init_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    res_id = env.ref(ref_menu)

    if len(res_id):
        res_id.groups_id = [(6, 0, [env.ref(group_id_new).id])]


def uninstall_hook(cr, registry):
    env = Environment(cr, SUPERUSER_ID, {})
    res_id = env.ref(ref_menu)

    groups_id = []
    for group_id in groups_ids: 
        groups_id.append(env.ref(group_id).id)

    if len(res_id):
        res_id.groups_id = [(6, 0, groups_id)]

