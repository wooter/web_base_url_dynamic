from odoo.tests import common

class TestWebBaseURL(common.TransactionCase):

    def test_base_url_fallback(self):
        # Fallback when no request
        icp = self.env['ir.config_parameter']
        url = icp.get_param("web.base.url")
        self.assertTrue(url.startswith("http"))
