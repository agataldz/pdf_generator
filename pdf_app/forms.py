from django import forms

from pdf_app.models import Pdf


class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
<<<<<<< HEAD
        exclude = ['file']
=======
        fields = '__all__'
>>>>>>> 4bfc297ccbc58127945e3cd8a15b9bc0cafcac09
