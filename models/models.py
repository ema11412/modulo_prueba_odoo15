#-*- coding: utf-8 -*-

from odoo import models, fields, api

# 
from datetime import datetime

'''
    Emanuel Esquivel Lopez
    Test Model
'''
class SaleOrder(models.Model):
    '''
    
        Modelo de los fields solicitados
            - Puse los campos requeridos.
        
        contrato_externo : Char
        fecha_de_contrato: Datetime

    '''

    # inherit para modificacion de sale.order
    _inherit = 'sale.order'

    contrato_externo = fields.Char("Contrato Externo", required=True)
    
    fecha_de_contrato = fields.Datetime('Fecha de contrato', default=datetime.today(), required=True )