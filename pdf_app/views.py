import uuid

from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

from pdf.settings import PDF_URL, PDF_ROOT
from pdf_app.forms import PdfForm
from pdf_app.tasks import generate_pdf


class PdfView(View):

    def post(self, request):

        form = PdfForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data['word']
            text = form.cleaned_data['text']
            number = form.cleaned_data['number']
            date = form.cleaned_data['date']

            file_name = str(uuid.uuid4())

            content = (word, text, number, date)
            generate_pdf.delay(content, file_name)

            url = PDF_URL + file_name

            return render(request, "pdf.html", {"form": form,
                                                "url": url})

        return HttpResponse("Wprowadzono nieprawidłowe dane")

    def get(self, request):

        form = PdfForm()
        return render(request, "pdf.html", {"form": form})


def download_pdf(request, file_name):

    path = PDF_ROOT + file_name
    file = open(path, 'rb')
    response = HttpResponse(file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename={}.pdf'.format(file_name)
    return response
