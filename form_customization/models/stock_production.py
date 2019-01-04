
from odoo import models, fields


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    production_date = fields.Date(
        'Production Date', default=fields.Datetime.now)
