from odoo import models,fields,api
from collections import defaultdict

class SelectedSaleReport(models.TransientModel):
    _name = 'sale.selected.report'

    sale_order = fields.Many2many('sale.order',string="Orders")
    product_categ = fields.Many2one('product.product')


    def generate_sale_pdf_report(self):
        result_dict = defaultdict(lambda: {'product': '','quantity': 0, 'demand': 0,'uom':'','category':''})
        orders = self.sale_order.order_line

        for line in orders:
            product_name = line.product_id.name
            result_dict[product_name]['name'] = product_name
            result_dict[product_name]['category'] = line.product_id.categ_id.name
            result_dict[product_name]['quantity'] += line.product_uom_qty
            result_dict[product_name]['demand'] += line.demand
            result_dict[product_name]['uom'] = line.product_uom.name

        result = dict(result_dict)

        print(result)
        data = {
            'form': self.read()[0],
            'dict1': result
        }
        return self.env.ref('filter_sales_product_report.filter_sale_product_report').report_action(self, data=data)
