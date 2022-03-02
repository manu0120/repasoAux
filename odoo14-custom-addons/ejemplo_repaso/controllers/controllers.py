# -*- coding: utf-8 -*-
# from odoo import http


# class EjemploRepaso(http.Controller):
#     @http.route('/ejemplo_repaso/ejemplo_repaso/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejemplo_repaso/ejemplo_repaso/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejemplo_repaso.listing', {
#             'root': '/ejemplo_repaso/ejemplo_repaso',
#             'objects': http.request.env['ejemplo_repaso.ejemplo_repaso'].search([]),
#         })

#     @http.route('/ejemplo_repaso/ejemplo_repaso/objects/<model("ejemplo_repaso.ejemplo_repaso"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejemplo_repaso.object', {
#             'object': obj
#         })
