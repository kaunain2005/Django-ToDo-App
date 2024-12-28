from django.urls import path
from .views import home, students, admit_student

app_name = 'core'

urlpatterns = [
    # /core/
    path('', home, name='home'),
    # /core/students
    path('students/', students, name='students'),
    # /core/students/admit
    path('students/admit/', admit_student, name='admit'),
]
