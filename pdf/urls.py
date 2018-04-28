from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path

from pdf import settings
from pdf_app.views import pdf_view, delete_pdf, download_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pdf_view, name = 'pdf'),
    re_path(r'^delete/(?P<id>(\d)+)$', delete_pdf, name='delete'),
    re_path(r'^media/files/(?P<file_name>[-\w]+)/$', download_pdf, name='pdf_downlaod')
] + static(settings.PDF_URL, document_root=settings.PDF_ROOT)
