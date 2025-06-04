from odoo import models
from odoo.http import request

class IrConfigParameter(models.Model):
    _inherit = "ir.config_parameter"

    def get_param(self, key, default=False):
        # Use the real request domain for web.base.url
        if key == "web.base.url" and request:
            try:
                return request.httprequest.url_root.rstrip("/")
            except Exception:
                pass
        return super().get_param(key, default)
