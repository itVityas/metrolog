from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import IndexView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='index', permanent=False)),
    path('index/', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('handbooks/', include('apps.handbooks.urls')),
]
