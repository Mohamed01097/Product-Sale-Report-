from odoo import api, fields, models, _


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    weight = fields.Float(string="weight")


    @api.onchange('product_uom')
    def set_weight(self):
        self.weight = self.product_uom.factor_inv


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'


    def button_confirm(self):
        res = super(PurchaseOrder,self).button_confirm()

        for pick in self.picking_ids.move_ids:
            pick.quantity = self.order_line.product_qty
            pick.weight = self.order_line.weight
            pick.price_unit = self.order_line.price_unit
            pick.product_uom = self.order_line.product_uom.id
        return res

class StockMove(models.Model):
    _inherit = 'stock.move'

    product_uom_qty = fields.Float(
        'Demand',
        digits='Product Unit of Measure',
        default=1.0, required=True, states={'done': [('readonly', True)]},
        help="This is the quantity of products from an inventory "
             "point of view. For moves in the state 'done', this is the "
             "quantity of products that were actually moved. For other "
             "moves, this is the quantity of product that is planned to "
             "be moved. Lowering this quantity does not generate a "
             "backorder. Changing this quantity on assigned moves affects "
             "the product reservation, and should be done with care.",compute='custom_set_product_uom_qty',store=True)


    @api.depends('weight','quantity')
    def custom_set_product_uom_qty(self):
        if self.weight and self.quantity:
            self.product_uom_qty = self.weight * self.quantity

    @api.onchange('product_uom')
    def set_weight(self):
        self.weight = self.product_uom.factor_inv

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    purchase_order_id = fields.Many2one('purchase.order')

    def button_validate(self):
        res = super(StockPicking,self).button_validate()
        for line in self.purchase_order_id.order_line:
            line.qty_received = self.move_ids.quantity_done
        return res
























    # def _prepare_stock_moves(self, picking):
    #     print("Called")
    #     res = super(PurchaseOrderLine, self)._prepare_stock_moves(picking)
    #     print("res.....",res)
    #     for move in res:
    #         move.update({
    #             'price_unit':self.price_unit,
    #             'quantity':self.product_qty,
    #             'weight':self.weight,
    #         })
    #     return res

    # def _prepare_stock_moves(self, picking):
    #     print("picking...........", picking)
    #     if self.order_id.state == 'purchase':
    #         res = super(PurchaseOrderLine, self)._prepare_stock_moves(picking)
    #         print("res............", res)
    #         print("price......", picking.move_ids_without_package)
    #         # lst_lines = []
    #         # Loop through the existing stock moves and update them
    #         for line in picking.move_ids_without_package:
    #             if line:
    #                 line.write({
    #                     'price_unit': self.price_unit,
    #                     'weight': self.weight,
    #                     'quantity': self.product_qty,
    #                 })
    #             for move in res:
    #                 move['price_unit'] = self.price_unit
    #                 move['weight'] = self.weight
    #                 move['quantity'] = self.product_qty
    #                 return res
    # def _prepare_stock_moves(self, picking):
    #     print("picking...........",picking)
    #     if self.order_id.state == 'purchase':
    #         res = super(PurchaseOrderLine, self)._prepare_stock_moves(picking)
    #         print("res............",res)
    #         print("price......",picking.move_ids_without_package)
    #
    #         # Loop through the existing stock moves and update them
    #         for line in picking.move_ids_without_package:
    #             if line:
    #                 print("old....",line.weight)
    #                 line.write({
    #                     'weight': self.weight,
    #                 })
    #                 print("new......",line.weight)
    #
    #             return res


