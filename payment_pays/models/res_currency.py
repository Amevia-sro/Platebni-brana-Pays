from odoo import fields, models


class ResCurrency(models.Model):
    _inherit = 'res.currency'

    currency_in_subunit = fields.Float('Currency Unit in Subunit', default=0.01)
