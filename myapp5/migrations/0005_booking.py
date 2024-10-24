# Generated by Django 5.0.4 on 2024-05-09 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0004_rename_dep_name_doctors_dep_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_name', models.CharField(max_length=255)),
                ('P_phone', models.CharField(max_length=10)),
                ('P_email', models.EmailField(max_length=254)),
                ('Booking_date', models.DateField()),
                ('Booked_on', models.DateField(auto_now=True)),
                ('Doc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp5.doctors')),
            ],
        ),
    ]
