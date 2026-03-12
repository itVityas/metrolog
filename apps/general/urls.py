from django.urls import path
from . import views


urlpatterns = [
     path('settings/<int:pk>/',
          views.SettingsUpdateView.as_view(),
          name='settings'),
]
