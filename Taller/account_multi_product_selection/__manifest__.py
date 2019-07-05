# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2017-Today Sitaram
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name':
    "Account Multi Product Selection",
    'version':
    "11.0.0.2",
    'summary':
    "Este modulo permite añadir varios productos filtrados en account invoice.",
    'category':
    'Sale Management',
    'description':
    """
        Este modulo permite añadir varios productos filtrados en account invoice
    """,
    'author':
    "Pereira",
    'website':
    " ",
    'depends': ['base', 'account', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale.xml',
    ],
    'demo': [],
    "license":
    "AGPL-3",
    'images': ['static/description/banner.png'],
    'live_test_url':
    'https://youtu.be/0KFUawEdMpk',
    'installable':
    True,
    'application':
    True,
    'auto_install':
    False,
}