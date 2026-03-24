from django.urls import path
from . import views


urlpatterns = [
     path('passport/',
          views.PassportDetailView.as_view(),
          name='passport'),
]
