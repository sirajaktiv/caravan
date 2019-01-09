
from odoo import models, fields


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    hijri_date = fields.Char(string="التاريخ")
    note_1 = fields.Text()
    note_2 = fields.Text()
    note_3 = fields.Text()
    note_4 = fields.Text()
