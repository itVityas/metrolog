from django.urls import path
from . import views


urlpatterns = [
     # passport main routes
     path('passport/',
          views.PassportListView.as_view(),
          name='passport'),

     path('passport/<int:pk>/',
          views.MocListDetailView.as_view(),
          name='passport_detail'),
     path('passport/add/',
          views.MocListCreateView.as_view(),
          name='passport_add'),
     path('passport/<int:pk>/update/',
          views.MocListUpdateView.as_view(),
          name='passport_update'),
     path('passport/<int:pk>/delete/',
          views.MocListDeleteView.as_view(),
          name='passport_delete'),

     # VerificationInfo routes
     path('passport/verification/add/',
          views.VerificationInfoCreateView.as_view(),
          name='verification_info_add'),
     path('passport/verification/<int:pk>/update/',
          views.VerificationInfoUpdateView.as_view(),
          name='verification_info_update'),
     path('passport/verification/<int:pk>/delete/',
          views.VerificationInfoDeleteView.as_view(),
          name='verification_info_delete'),

     # RepairInfo routes
     path('passport/repair/add/',
          views.RepairInfoCreateView.as_view(),
          name='repair_info_add'),
     path('passport/repair/<int:pk>/update/',
          views.RepairInfoUpdateView.as_view(),
          name='repair_info_update'),
     path('passport/repair/<int:pk>/delete/',
          views.RepairInfoDeleteView.as_view(),
          name='repair_info_delete'),

     # DeviceLocation routes
     path('passport/location/add/',
          views.DeviceLocationCreateView.as_view(),
          name='device_location_add'),
     path('passport/location/<int:pk>/update/',
          views.DeviceLocationUpdateView.as_view(),
          name='device_location_update'),
     path('passport/location/<int:pk>/delete/',
          views.DeviceLocationDeleteView.as_view(),
          name='device_location_delete'),

     # DeviceStatusDate routes
     path('passport/status/add/',
          views.DeviceStatusDateCreateView.as_view(),
          name='device_status_date_add'),
     path('passport/status/<int:pk>/update/',
          views.DeviceStatusDateUpdateView.as_view(),
          name='device_status_date_update'),
     path('passport/status/<int:pk>/delete/',
          views.DeviceStatusDateDeleteView.as_view(),
          name='device_status_date_delete'),

     # MocMetals routes
     path('passport/metall/add/',
          views.MocMetalsCreateView.as_view(),
          name='moc_metals_add'),
     path('passport/metall/<int:pk>/update/',
          views.MocMetalsUpdateView.as_view(),
          name='moc_metals_update'),
     path('passport/metall/<int:pk>/delete/',
          views.MocMetalsDeleteView.as_view(),
          name='moc_metals_delete'),
]
