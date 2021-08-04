# -*- coding: utf-8 -*-
# Developer: Carlos Avila.
# Mail: car.josavica@gmail.com
# Boostech CR
# 21.07.13

{
    'name' : 'Pure Life AO 1',
    'version' : '21.07.13',
    'summary': 'Pasar información del formulario Web',
    'sequence': 0,
    'description': """
Contiene
====================

    Información adicional en formulario de oportunidades

    Datos:
    * Nombre del Paciente
    * PLA Service

    
    
    """,
    'category': 'AddOns',
    'author': "Boostech CR",
    'website': 'https://boostechcr.com/',
    'images' : [
    ],
    'depends' : [
        'crm',
        'sale_management',
        'account',
        'sale_crm'
    ],
    'data': [
        'views_inherits/views_bt_crm_lead.xml',
        'views_inherits/views_bt_sale_order.xml',
        
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
