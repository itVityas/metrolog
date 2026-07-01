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

     # creating modals in passport
     path('passport/passport_moc_type_add/',
          views.PassportMocTypeView.as_view(),
          name='passport_moc_type'),
     path('passport/passport_change_type_add/',
          views.PassportChangeTypeView.as_view(),
          name='passport_change_type'),
     path('passport/passport_moc_group_add/',
          views.PassportMocGroupView.as_view(),
          name='passport_moc_group'),
     path('passport/passport_verification_department_add/',
          views.PassportVerificationDepartmentView.as_view(),
          name='passport_verification_department'),

     # creating modals in passport for verification
     path('passport/passport_verification_person/',
          views.PassportVerificationPersonView.as_view(),
          name='passport_verification_person'),
     path('passport/passport_verification_sign/',
          views.PassportVerificationSignView.as_view(),
          name='passport_verification_sign'),

     # creating modals in passport for repair
     path('passport/passport_repair/',
          views.PassportRepairView.as_view(),
          name='passport_repair'),
     path('passport/passport_repair_code/',
          views.PassportRepairCodeView.as_view(),
          name='passport_repair_code'),
     path('passport/passport_repair_department/',
          views.PassportRepairDepartmentView.as_view(),
          name='passport_repair_department'),
     path('passport/passport_instrument_failure/',
          views.PassportInstrumentFailureView.as_view(),
          name='passport_instrument_failure'),

     # creating modals in passport for location
     path('passport/passport_department/',
          views.PassportDepartmentView.as_view(),
          name='passport_department'),

     # creating modals in passport for status
     path('passport/passport_device_status/',
          views.PassportDeviceStatusView.as_view(),
          name='passport_device_status'),

     # creating modals in passport for metall
     path('passport/passport_precious_metals/',
          views.PassportPreciousMetalsView.as_view(),
          name='passport_precious_metals'),

     path('passport/migrate/',
          views.PassportMigrateView.as_view(),
          name='passport_migrate'),

     path('passport/<int:pk>/print/',
          views.PassportPrintView.as_view(),
          name='passport_print'),

     # VerificationInfo routes
     path('passport/<int:passport>/verification/add/',
          views.VerificationInfoCreateView.as_view(),
          name='verification_info_add'),
     path('passport/<int:passport>/verification/<int:pk>/update/',
          views.VerificationInfoUpdateView.as_view(),
          name='verification_info_update'),
     path('passport/<int:passport>/verification/<int:pk>/delete/',
          views.VerificationInfoDeleteView.as_view(),
          name='verification_info_delete'),

     # RepairInfo routes
     path('passport/<int:passport>/repair/add/',
          views.RepairInfoCreateView.as_view(),
          name='repair_info_add'),
     path('passport/<int:passport>/repair/<int:pk>/update/',
          views.RepairInfoUpdateView.as_view(),
          name='repair_info_update'),
     path('passport/<int:passport>/repair/<int:pk>/delete/',
          views.RepairInfoDeleteView.as_view(),
          name='repair_info_delete'),

     # DeviceLocation routes
     path('passport/<int:passport>/location/add/',
          views.DeviceLocationCreateView.as_view(),
          name='device_location_add'),
     path('passport/<int:passport>/location/<int:pk>/update/',
          views.DeviceLocationUpdateView.as_view(),
          name='device_location_update'),
     path('passport/<int:passport>/location/<int:pk>/delete/',
          views.DeviceLocationDeleteView.as_view(),
          name='device_location_delete'),

     # DeviceStatusDate routes
     path('passport/<int:passport>/status/add/',
          views.DeviceStatusDateCreateView.as_view(),
          name='device_status_date_add'),
     path('passport/<int:passport>/status/<int:pk>/update/',
          views.DeviceStatusDateUpdateView.as_view(),
          name='device_status_date_update'),
     path('passport/<int:passport>/status/<int:pk>/delete/',
          views.DeviceStatusDateDeleteView.as_view(),
          name='device_status_date_delete'),

     # MocMetals routes
     path('passport/<int:passport>/metall/add/',
          views.MocMetalsCreateView.as_view(),
          name='moc_metals_add'),
     path('passport/<int:passport>/metall/<int:pk>/update/',
          views.MocMetalsUpdateView.as_view(),
          name='moc_metals_update'),
     path('passport/<int:passport>/metall/<int:pk>/delete/',
          views.MocMetalsDeleteView.as_view(),
          name='moc_metals_delete'),
]
