from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView)
from django.urls import path


urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='login.html'),
         name='login'
         ),
    path('logout/',
         LogoutView.as_view(next_page='login'),
         name='logout'
         ),
    path('password_change/',
         PasswordChangeView.as_view(template_name='password_change_form.html'),
         name='password_change'
         ),
    path('password_change/done/',
         PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'
         ),
]
