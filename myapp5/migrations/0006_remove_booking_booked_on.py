# Generated by Django 5.0.4 on 2024-05-12 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0005_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Booked_on',
        ),
    ]
