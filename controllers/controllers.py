# -*- coding: utf-8 -*-
# from odoo import http


# class BookshopApp(http.Controller):
#     @http.route('/bookshop_app/bookshop_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bookshop_app/bookshop_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bookshop_app.listing', {
#             'root': '/bookshop_app/bookshop_app',
#             'objects': http.request.env['bookshop_app.bookshop_app'].search([]),
#         })

#     @http.route('/bookshop_app/bookshop_app/objects/<model("bookshop_app.bookshop_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bookshop_app.object', {
#             'object': obj
#         })
