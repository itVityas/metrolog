from django.urls import path
from . import views


urlpatterns = [
     path('passport/<int:pk>/',
          views.PassportDetailView.as_view(),
          name='passport'),
]
