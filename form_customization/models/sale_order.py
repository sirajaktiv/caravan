
from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    lot_number = fields.Many2one('stock.production.lot', string='Lot Number')
    production_date = fields.Date(
        'Production date', related='lot_number.production_date')
    expiry_date = fields.Datetime(
        'Expiry date', related='lot_number.life_date')
