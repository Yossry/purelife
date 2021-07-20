# -*- coding: utf-8 -*-
# Developer: Carlos Avila.
# Mail: car.josavica@gmail.com
# Boostech CR
# 21.07.13

{
    'name' : 'Menu Especial - Contactos',
    'version' : '21.07.13',
    'summary': 'Bloquea el menú Contactos',
    'sequence': 0,
    'description': """
Contiene
====================

    Bloquea el menú Contactos
    
    """,
    'category': 'AddOns',
    'author': "Boostech CR",
    'website': 'https://boostechcr.com/',
    'images' : [
    ],
    'depends' : [
        'base',
        'bt_menu_special',
    ],
    'data': [
        'security/security.xml'
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'qweb': [],
}
