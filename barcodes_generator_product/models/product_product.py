# Copyright (C) 2014-Today GRAP (http://www.grap.coop)
# Copyright (C) 2016-Today La Louve (http://www.lalouve.net)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models


class ProductProduct(models.Model):
    _name = 'product.product'
    _inherit = ['product.product', 'barcode.generate.mixin']

    def create(self, vals):
        record = super(ProductProduct, self).create(vals)

        if record and record.categ_id and not record.barcode:
            record.barcode_rule_id = record.categ_id.barcode_rule_id
            record.generate_base()
            record.generate_barcode()

        return record
