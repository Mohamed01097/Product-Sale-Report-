

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class StockMove(models.Model):
    _inherit = "stock.move"

    quantity = fields.Float(
        string="الكمية",
        store=True)
    weight = fields.Float("الوزن")
    price_unit = fields.Float("سعر الوحدة")
    # product_uom_qty = fields.Float('Demand',required=True,compute='set_demand',states={'done': [('readonly', True)]})


    # qty_available = fields.Float('Quantity',related= 'product_id.stock_quant_ids.quantity' )

    # @api.depends('weight','quantity')
    # def set_demand(self):
    #     for line in self:
    #         line.product_uom_qty = line.weight * line.quantity



