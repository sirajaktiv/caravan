from odoo import api, models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    arabic_company_name = fields.Char(string="Arabic Company Name")
    arabic_street = fields.Char(string="Address")
    arabic_street2 = fields.Char()
    arabic_city = fields.Char()
    arabic_country = fields.Char()
    arabic_state = fields.Char()
    arabic_email = fields.Char(string="Email")
    arabic_website = fields.Char(string="Website")
    arabic_zip = fields.Char()
    arabic_phone = fields.Char(string="Phone")

    @api.multi
    def _get_company_data(self, data):
        vals = []
        if data:
            for each in range(int(data.count(',')) + 1):
                vals.append(data.split(',')[each])
        return vals
