# Generated by Django 5.0.4 on 2025-03-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('roll', models.IntegerField()),
                ('class_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=11)),
                ('student', models.ManyToManyField(to='first_app.student')),
            ],
        ),
    ]
