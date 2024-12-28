from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # /admin/
    path('admin/', admin.site.urls),
    # /core/
    path('core/', include('core.urls', namespace='core')),
    # /accounts/
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # /todo/
    path('todo/', include('todo.urls', namespace='todo')),
]
