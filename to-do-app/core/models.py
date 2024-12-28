from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    student_id = models.CharField(max_length=50, unique=True)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.name}"
