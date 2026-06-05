from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...passport import models as pmodels
from django.shortcuts import render
from ..forms import OperatingTimeForm
from calendar import monthrange


class OperatingTimeView(LoginRequiredMixin, TemplateView):
    """
        Накопительная наработка прибориста
    """
    template_name = 'references/operating_time.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        form = OperatingTimeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']

        _, num_days = monthrange(start_date.year, start_date.month)
        end_date = start_date.replace(day=num_days)

        queryset = pmodels.VerificationInfo.objects.prefetch_related(
            'moc_list'
                ).filter(
                    verification_date__range=[
                        start_date,
                        end_date]).order_by(
                            'verification_date')
        result_list = []
        ver_bool_result = False
        for q in queryset:
            if q.verification_result == '1':
                ver_bool_result = True
            result_list.append({'result': ver_bool_result,
                                'values': q})
            ver_bool_result = False

        context['start_date'] = start_date
        context['queryset'] = result_list
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = OperatingTimeForm()
        return render(request,
                      'references/modals/operating_time_modal.html',
                      {'form': form})
