# Generated by Django 5.0.4 on 2024-05-23 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp5', '0010_add_patients_age_add_patients_age_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_patients',
            old_name='Age_unit',
            new_name='Age_category',
        ),
    ]
