from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.category'

    barcode_rule_id = fields.Many2one(
        string='Barcode Rule', readonly=False, comodel_name='barcode.rule')

