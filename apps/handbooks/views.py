from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MocGroup


class MocGroupListView(LoginRequiredMixin, ListView):
    model = MocGroup

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        verbose_names = {}
        for field in self.model._meta.get_fields():
            if hasattr(field, 'verbose_name'):
                verbose_names[field.name] = field.verbose_name
        context['verbose_names'] = verbose_names
        return context


class MocGroupAddView(LoginRequiredMixin, DetailView):
    pass


class MocGroupEditView(LoginRequiredMixin, DetailView):
    pass


class MocGroupDeleteView(LoginRequiredMixin, View):
    pass
