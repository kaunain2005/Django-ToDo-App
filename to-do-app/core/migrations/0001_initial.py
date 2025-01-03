# Generated by Django 5.0 on 2023-12-30 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('student_id', models.CharField(max_length=50, unique=True)),
                ('enrollment_date', models.DateField()),
            ],
        ),
    ]
