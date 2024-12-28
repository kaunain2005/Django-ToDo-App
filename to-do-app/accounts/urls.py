from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import signup

app_name = 'accounts'

urlpatterns = [
    # /accounts/signup/
    path('signup/', signup, name='signup'),
    # /accounts/login/
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # /accounts/logout/
    path('logout/', LogoutView.as_view(), name='logout'),
]
