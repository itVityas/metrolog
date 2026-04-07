from .passport import (PassportListView,
                       MocListDetailView,
                       MocListCreateView,
                       MocListUpdateView,
                       MocListDeleteView,
                       PassportMigrateView,
                       PassportPrintView)
from .verification_info import (VerificationInfoCreateView,
                                VerificationInfoDeleteView,
                                VerificationInfoUpdateView)
from .repair_info import (RepairInfoCreateView,
                          RepairInfoDeleteView,
                          RepairInfoUpdateView)
from .device_location import (DeviceLocationCreateView,
                              DeviceLocationDeleteView,
                              DeviceLocationUpdateView)
from .device_status_date import (DeviceStatusDateCreateView,
                                 DeviceStatusDateDeleteView,
                                 DeviceStatusDateUpdateView)
from .moc_metals import (MocMetalsCreateView,
                         MocMetalsDeleteView,
                         MocMetalsUpdateView)
