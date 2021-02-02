# -*- coding: utf-8 -*-
# Copyright 2019 Simone Rubino - Agile Business Group
# Copyright 2015 Camilli Alessandro - www.openforce.it
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "ITA - Intrastat",
    'version': '10.0.1.0.3',
    'category': 'Account',
    'summary': 'Riclassificazione merci e servizi per dichiarazioni Intrastat',
    'author': "Openforce, Link IT srl, Agile Business Group, "
              "Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/l10n-italy/tree/'
               '10.0/l10n_it_intrastat',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'product',
        'report_intrastat',
        'stock',
        'stock_account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/account.intrastat.transaction.nature.csv',
        'data/account.intrastat.transport.csv',
        'data/account.intrastat.custom.csv',
        'data/report.intrastat.code.csv',
        'views/intrastat.xml',
        'views/product.xml',
        'views/account.xml',
        'views/config.xml',
    ],
    'demo': [
        'demo/product_demo.xml'
    ]
}
