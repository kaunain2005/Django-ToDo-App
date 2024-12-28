from django.urls import path
from .views import home, toggle

app_name = 'todo'

urlpatterns = [
    # /todo/
    path('', home, name='home'),
    # /todo/toggle/
    path('toggle/<int:todo_id>/', toggle, name='toggle'),
]
