# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FilterSaleProduct(models.Model):
    _inherit = 'sale.order'

    my_field = fields.Many2many('sale.selected.report',string="Assosiated Field")



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    demand = fields.Float(string="Demand",store=True)

    @api.onchange('product_uom','product_uom_qty')
    def set_demand(self):
        self.demand = self.product_uom.factor_inv * self.product_uom_qty














# def filter_sales_products(self):
    #     for rec in self:
    #         res_dict = {}
    #         orders = rec.env['sale.order.line'].search([('order_id.state', '=', 'draft')])
    #         filtered_lines = orders.mapped('product_id')
    #         for product in filtered_lines:
    #             quantity = 0
    #             for line in orders:
    #                 if line.product_id == product:
    #                     quantity += line.demand
    #             res_dict[product] = quantity
    #
    #         sorted_dict = sorted(res_dict.items(), key=lambda item: item[1])
    #
    #         return dict(sorted_dict)
    #
    # def return_date_today(self):
    #     return date.today()