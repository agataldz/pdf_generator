from celery.task.base import task
from reportlab.pdfgen import canvas


from pdf.settings import PDF_ROOT


@task()
def generate_pdf(content, file_name):

    pdf = canvas.Canvas(PDF_ROOT + file_name)

    for i, item in enumerate(content):
        pdf.drawString(10, 800 - i * 10, str(item))

    pdf.showPage()
    pdf.save()
