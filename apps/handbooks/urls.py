from django.urls import path
from . import views


urlpatterns = [
    path('moc_group/',
         views.MocGroupListView.as_view(
             template_name='handbooks/tables/moc_group_table.html'
             ),
         name='moc_group'),
]
