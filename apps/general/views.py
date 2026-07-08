from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserSettings
from .forms import UserSettingsForm
from django.views.generic import View
import io
import json
from django.shortcuts import redirect
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from django.http import HttpResponse
from weasyprint import HTML
from pdf2docx import Converter


class SettingsUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for UserSettings
    """
    model = UserSettings
    form_class = UserSettingsForm
    template_name = 'general/settings.html'

    def get_success_url(self):
        return self.request.path


class SetPaginationView(LoginRequiredMixin, View):
    """
        Set pagination with page reload
    """
    def post(self, request, *args, **kwargs):
        form = UserSettingsForm(request.POST)
        pk = self.kwargs.get('pk')

        if form.is_valid():
            UserSettings.objects.filter(
                id=pk
                ).update(
                    pagination_size=form.cleaned_data['pagination_size'])

        raw_url = request.META.get('HTTP_REFERER', '/')

        url_parts = list(urlparse(raw_url))
        query_params = parse_qs(url_parts[4])
        query_params['page'] = 1
        url_parts[4] = urlencode(query_params, doseq=True)
        final_url = urlunparse(url_parts)

        return redirect(final_url)


class PrintToDocxView(LoginRequiredMixin, View):
    """
        View for printing HTML to DOCX
    """
    def post(self, request, *args, **kwargs):
        post_data = json.loads(request.body)
        html_data = post_data.get('html_to_print')

        html = HTML(string=html_data, base_url=request.build_absolute_uri())
        pdf_buffer = io.BytesIO(html.write_pdf())

        docx_buffer = io.BytesIO()

        cv = Converter(stream=pdf_buffer)
        cv.convert(docx_buffer, start=0, end=None)
        cv.close()

        docx_buffer.seek(0)

        response = HttpResponse(
            docx_buffer.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = 'attachment; filename="document.docx"'

        return response


class PrintToPDFView(LoginRequiredMixin, View):
    """
        View for printing HTML to PDF
    """
    def post(self, request, *args, **kwargs):

        post_data = json.loads(request.body)

        html_data = post_data.get('html_to_print')

        html = HTML(string=html_data, base_url=request.build_absolute_uri())
        pdf_bytes = html.write_pdf()

        response = HttpResponse(pdf_bytes, content_type='application/pdf')

        # Force download instead of opening in the browser
        # response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
        # response['Content-Disposition'] = 'inline; filename="invoice.pdf"'

        return response
