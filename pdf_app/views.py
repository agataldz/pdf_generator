import uuid


from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy


from pdf.settings import PDF_URL, PDF_ROOT
from pdf_app.forms import PdfForm
from pdf_app.models import Pdf
from pdf_app.tasks import generate_pdf


def pdf_view(request):

    files_all = Pdf.objects.all().order_by('-created')

    if request.method == "POST":

        form = PdfForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data['word']
            text = form.cleaned_data['text']
            number = form.cleaned_data['number']
            date = form.cleaned_data['date']

            file_name = str(uuid.uuid4())
            pdf_file = Pdf.objects.create(word=word,
                                          text=text,
                                          number=number,
                                          date=date)
            path = PDF_URL + file_name
            pdf_file.file = path
            pdf_file.save()

            content = (word, text, number, date)
            generate_pdf.delay(content, file_name)

            return render(request, "pdf.html", {"form": form,
                                                "files_all": files_all})

        return HttpResponse("Wprowadzono nieprawidłowe dane")

    else:

        form = PdfForm()
        return render(request, "pdf.html", {"form": form,
                                            "files_all": files_all})


def download_pdf(request, file_name):

    path = PDF_ROOT + file_name
    file = open(path, 'rb')
    response = HttpResponse(file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename={}.pdf'.format(file_name)
    return response


def delete_pdf(request, id):

    Pdf.objects.get(id=id).delete()
    return redirect(reverse_lazy('pdf'))
