from django.urls import path
from . import views


urlpatterns = [
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
]
