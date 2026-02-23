from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MocGroup
from .forms import MocGroupForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string


class MocGroupGetView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        moc_group_id = kwargs.get('pk')
        if not moc_group_id:
            new_form = MocGroupForm()
            context = {'form': new_form}
            html = render_to_string(
                'handbooks/forms/moc_group_form.html',
                context,
                request=request)
            return HttpResponse(html)
        else:
            moc_group = MocGroup.objects.get(id=moc_group_id)
            new_form = MocGroupForm(instance=moc_group)
            context = {'form': new_form}
            html = render_to_string(
                'handbooks/forms/moc_group_form.html',
                context,
                request=request)
            return HttpResponse(html)


class MocGroupListView(LoginRequiredMixin, ListView):
    model = MocGroup
    template_name = 'handbooks/tables/moc_group_table.html'
    form = MocGroupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        context['form'] = MocGroupForm
        return context


class MocGroupAddView(LoginRequiredMixin, CreateView):
    model = MocGroup
    form_class = MocGroupForm
    success_url = reverse_lazy('moc_group')


class MocGroupUpdateView(LoginRequiredMixin, UpdateView):
    model = MocGroup
    form_class = MocGroupForm
    success_url = reverse_lazy('moc_group')


class MocGroupDeleteView(LoginRequiredMixin, DeleteView):
    model = MocGroup
    form_class = MocGroupForm
    success_url = reverse_lazy('moc_group')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
