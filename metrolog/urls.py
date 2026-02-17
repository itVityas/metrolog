from django.contrib import admin
from django.urls import path, include
from apps.accounts.views import IndexView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls'))
]
