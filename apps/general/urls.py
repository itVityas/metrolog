from django.urls import path
from . import views


urlpatterns = [
     path('settings/<int:pk>/',
          views.SettingsUpdateView.as_view(),
          name='settings'),
     path('print_to_docx/',
          views.PrintToDocxView.as_view(),
          name='print_to_docx'),
]
