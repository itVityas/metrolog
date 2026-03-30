from django.urls import path
from . import views


urlpatterns = [
     path('passport/',
          views.PassportDetailView.as_view(),
          name='passport'),
     path('passport/add/',
          views.MocListCreateView.as_view(),
          name='passport_add'),
     path('passport/<int:pk>/update/',
          views.MocListUpdateView.as_view(),
          name='passport_update'),
     path('passport/<int:pk>/delete/',
          views.MocListDeleteView.as_view(),
          name='passport_delete'),
]
