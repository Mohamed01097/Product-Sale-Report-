# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseModify(http.Controller):
#     @http.route('/purchase_modify/purchase_modify', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_modify/purchase_modify/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_modify.listing', {
#             'root': '/purchase_modify/purchase_modify',
#             'objects': http.request.env['purchase_modify.purchase_modify'].search([]),
#         })

#     @http.route('/purchase_modify/purchase_modify/objects/<model("purchase_modify.purchase_modify"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_modify.object', {
#             'object': obj
#         })
