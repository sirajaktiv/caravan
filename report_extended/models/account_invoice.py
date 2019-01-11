
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


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def get_tax_recs(self, rec):
        tax_list = rec.invoice_line_ids.mapped(
            'invoice_line_tax_ids').mapped('name')
        return tax_list

    @api.multi
    def get_arabic_numbers(self, number):
        if number:
            number_list = [int(x) for x in str(number)]
            arabic_num_dict = {
                0: '٠', 1: '١', 2: '٢', 3: '٣', 4: '٤', 5: '٥',
                6: '٦', 7: '٧', 8: '٨', 9: '٩'}
            arabic_num_list = [arabic_num_dict[x] for x in number_list]
            arabic_number = ''.join(arabic_num_list)
            return arabic_number
        return False


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
