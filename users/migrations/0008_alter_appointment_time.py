# Generated by Django 4.0.2 on 2022-02-14 22:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_appointment_time_alter_appointment_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]