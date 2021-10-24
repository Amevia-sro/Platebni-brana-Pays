# -*- coding: utf-8 -*-

{
    'name': 'Pays Payment Gateway',
    'version': '1.0',
    'summary': 'Payment Gateway integration for Czech Republic',
    'author': 'Amevia s.r.o.',
    "website" : "https://www.amevia.eu",
    'description': """Configuration of Czech gateway Pays""",
    'category': 'Payment Gateway: Pays Implementation',
    'depends': ['payment'],
    'data': [
        'views/payment_pays_template.xml',
        'views/payment_views.xml',
        'views/currency_views.xml',
        'data/payment_acquirer_data.xml',
    ],
}
