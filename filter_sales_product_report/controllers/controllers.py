# -*- coding: utf-8 -*-
# from odoo import http


# class FilterSalesProductReport(http.Controller):
#     @http.route('/filter_sales_product_report/filter_sales_product_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filter_sales_product_report/filter_sales_product_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('filter_sales_product_report.listing', {
#             'root': '/filter_sales_product_report/filter_sales_product_report',
#             'objects': http.request.env['filter_sales_product_report.filter_sales_product_report'].search([]),
#         })

#     @http.route('/filter_sales_product_report/filter_sales_product_report/objects/<model("filter_sales_product_report.filter_sales_product_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filter_sales_product_report.object', {
#             'object': obj
#         })
