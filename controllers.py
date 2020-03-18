# -*- coding: utf-8 -*-
# from odoo import http


# class Custom-addons/xxCustom-shipping(http.Controller):
#     @http.route('/custom-addons/xx_custom-shipping/custom-addons/xx_custom-shipping/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom-addons/xx_custom-shipping/custom-addons/xx_custom-shipping/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom-addons/xx_custom-shipping.listing', {
#             'root': '/custom-addons/xx_custom-shipping/custom-addons/xx_custom-shipping',
#             'objects': http.request.env['custom-addons/xx_custom-shipping.custom-addons/xx_custom-shipping'].search([]),
#         })

#     @http.route('/custom-addons/xx_custom-shipping/custom-addons/xx_custom-shipping/objects/<model("custom-addons/xx_custom-shipping.custom-addons/xx_custom-shipping"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom-addons/xx_custom-shipping.object', {
#             'object': obj
#         })
