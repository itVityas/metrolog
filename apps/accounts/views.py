from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context=None)
