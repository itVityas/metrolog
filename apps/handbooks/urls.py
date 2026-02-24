from django.urls import path
from . import views


urlpatterns = [
     # url paths for MocGroup
     path('moc_group/',
          views.MocGroupListView.as_view(),
          name='moc_group'),
     path('moc_group/add/',
          views.MocGroupAddView.as_view(),
          name='moc_group_add'),
     path('moc_group/<int:pk>/update/',
          views.MocGroupUpdateView.as_view(),
          name='moc_group_update'),
     path('moc_group/<int:pk>/delete/',
          views.MocGroupDeleteView.as_view(),
          name='moc_group_delete'),

     # url paths for ChangeType
     path('change_type/',
          views.ChangeTypeListView.as_view(),
          name='change_type'),
     path('change_type/add/',
          views.ChangeTypeAddView.as_view(),
          name='change_type_add'),
     path('change_type/<int:pk>/update/',
          views.ChangeTypeUpdateView.as_view(),
          name='change_type_update'),
     path('change_type/<int:pk>/delete/',
          views.ChangeTypeDeleteView.as_view(),
          name='change_type_delete'),
]
