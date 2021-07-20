# -*- coding: utf-8 -*-
# Developer: Carlos Avila.
# Mail: car.josavica@gmail.com
# Boostech CR
# 21.07.13

{
    'name' : 'MRP AO 1',
    'version' : '21.07.13',
    'summary': 'Bloquea a los usuario para ver ordenes de trabajo por Centro de Trabajo',
    'sequence': 0,
    'description': """
Contiene
====================

    Bloquea a los usuario para ver ordenes de trabajo por Centro de Trabajo

    Para habilitar el bloqueo debe:
    * Habilitar la opción de bloqueo en el usuario
    * Agrega al usuario al Centro de Trabajo
    
    """,
    'category': 'AddOns',
    'author': "Boostech CR",
    'website': 'https://boostechcr.com/',
    'images' : [
    ],
    'depends' : [
        'mrp',
        'base',
    ],
    'data': [
        'views_inherits/views_bt_mrp_workcenter.xml',
        
        'security/security.xml',
        
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
