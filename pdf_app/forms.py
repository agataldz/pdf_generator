from django import forms

from pdf_app.models import Pdf


class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        exclude = ['file']
