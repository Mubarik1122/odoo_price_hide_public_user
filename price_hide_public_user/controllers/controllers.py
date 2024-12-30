# -*- coding: utf-8 -*-
from odoo import http


class PriceHidePublicUser(http.Controller):
    @http.route('/price_hide_public_user/price_hide_public_user', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/price_hide_public_user/price_hide_public_user/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('price_hide_public_user.listing', {
#             'root': '/price_hide_public_user/price_hide_public_user',
#             'objects': http.request.env['price_hide_public_user.price_hide_public_user'].search([]),
#         })

#     @http.route('/price_hide_public_user/price_hide_public_user/objects/<model("price_hide_public_user.price_hide_public_user"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('price_hide_public_user.object', {
#             'object': obj
#         })
