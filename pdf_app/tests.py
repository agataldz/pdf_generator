import unittest

from django.test import TestCase

from pdf_app.forms import PdfForm


class PdfTest (TestCase):
    def test_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_form(self):
        form_data = {'word': 'word',
                     'text': 'text',
                     'number': '1234',
                     'date': '2018-04-29'}
        form = PdfForm(data=form_data)
        self.assertTrue(form.is_valid())

if __name__ == '__main__':
    unittest.main()
