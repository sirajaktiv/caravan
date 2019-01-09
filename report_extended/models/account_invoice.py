
from odoo import models, fields, api
from odoo.tools import float_is_zero
from googletrans import Translator


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    lot_number = fields.Many2one('stock.production.lot', string='Lot Number')
    production_date = fields.Date(
        'Production date', related='lot_number.production_date')
    expiry_date = fields.Datetime(
        'Expiry date', related='lot_number.life_date')


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.multi
    def invoice_line_create(self, invoice_id, qty):
        """ Create an invoice line. The quantity to invoice can be positive
        (invoice) or negative (refund).
            :param invoice_id: integer
            :param qty: float quantity to invoice
            :returns recordset of account.invoice.line created
        """
        invoice_lines = self.env['account.invoice.line']
        precision = self.env['decimal.precision'].precision_get(
            'Product Unit of Measure')
        for line in self:
            if not float_is_zero(qty, precision_digits=precision):
                vals = line._prepare_invoice_line(qty=qty)
                vals.update({'invoice_id': invoice_id,
                             'lot_number': line.lot_number.id,
                             'sale_line_ids': [(6, 0, [line.id])]})
                invoice_lines |= self.env['account.invoice.line'].create(vals)
        return invoice_lines


class ResCompany(models.Model):
    _inherit = "res.company"

    @api.multi
    def _get_company_data(self, data):
        vals = []
        for each in range(int(data.count(',')) + 1):
            vals.append(data.split(',')[each])
        return vals

    @api.multi
    def _get_company_details_arabic(self, data):
        translator = Translator()
        if data:
            name = translator.translate(data, dest='arabic').text
            return name
        return data
