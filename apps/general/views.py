from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserSettings
from .forms import UserSettingsForm


class SettingsUpdateView(LoginRequiredMixin, UpdateView):
    """
        UpdateView for UserSettings
    """
    model = UserSettings
    form_class = UserSettingsForm
    template_name = 'general/settings.html'

    def get_success_url(self):
        return self.request.path
