from django.urls import path
from . import views


urlpatterns = [
     path('settings/<int:pk>/',
          views.SettingsUpdateView.as_view(),
          name='settings'),
     path('set_pagination/<int:pk>/',
          views.SetPaginationView.as_view(),
          name='set_pagination'),
     path('print_to_docx/',
          views.PrintToDocxView.as_view(),
          name='print_to_docx'),
]
