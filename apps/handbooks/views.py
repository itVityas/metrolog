from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MocGroup
from .forms import MocGroupForm
from django.http import HttpResponseRedirect


class MocGroupListView(LoginRequiredMixin, ListView):
    model = MocGroup
    template_name = 'handbooks/tables/moc_group_table.html'
    form = MocGroupForm
    paginate_by = 15

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
