from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserSettings
from .forms import UserSettingsForm
from django.views.generic import View
from docx import Document
from html4docx import HtmlToDocx
from django.http import FileResponse
import io
import json
from django.shortcuts import redirect
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


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
        doc = Document()
        parser = HtmlToDocx()

        post_data = json.loads(request.body)

        html_data = post_data.get('html_to_print')
        file_name = post_data.get('name')
        print('html_data = ' + html_data)
        print('file_name = ' + file_name)

        parser.add_html_to_document(html_data, doc)

        buffer = io.BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        response = FileResponse(
            buffer,
            as_attachment=True,
            filename=file_name,
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        return response
