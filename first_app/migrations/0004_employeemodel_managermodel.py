# Generated by Django 5.0.4 on 2025-03-08 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_remove_teacherinfomodel_roll'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ManagerModel',
            fields=[
                ('employeemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='first_app.employeemodel')),
                ('take_interview', models.BooleanField()),
                ('hiring', models.BooleanField()),
            ],
            bases=('first_app.employeemodel',),
        ),
    ]
