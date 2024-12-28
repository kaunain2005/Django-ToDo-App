from django import forms
from .models import Student


class StudentAdmissionForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'age', 'enrollment_date']
