from urllib.parse import urlencode

from odoo import fields, models, _
from odoo.exceptions import UserError


class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('pays', 'Pays.cz')])
    merchant_id = fields.Char('Merchant Identifier')
    eshop_id = fields.Char('E-shop Identifier')

    def pays_form_generate_values(self, values):
        if not self.merchant_id or not self.eshop_id:
            raise UserError(_('Please configure merchant/eshop identifier in Pays.cz acquirer.'))
        url = 'https://www.pays.cz/paymentorder?'
        query_string_dict = {
            'Merchant': self.merchant_id,
            'Shop': self.eshop_id,
            'Amount': int(values['amount'] / values['currency'].currency_in_subunit),
            'Currency': values['currency'].name,
            'MerchantOrderNumber': values['reference'],
            'Email': values['partner'].email or '',
        }
        query_string = urlencode(query_string_dict)
        url += query_string
        pays_values = dict(values, pays_tx_url=url)
        return pays_values
