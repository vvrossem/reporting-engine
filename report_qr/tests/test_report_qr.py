# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import HttpCase


class TestReportQr(HttpCase):

    def test_qr_generation(self):
        data = 'TEST'
        image = self.url_open('/report/qr?value=%s' % data)
        self.assertEqual(image.headers['Content-type'], 'image/png')

    def test_qr_overflow(self):
        """There is a QR limitation for 4296 characters, we will test that an
        Exception is raised"""
        new_data = ''
        for i in range(0, 1500):
            new_data += 'TEST'
        with self.assertRaises(Exception):
            self.env['report'].qr_generate(new_data)
