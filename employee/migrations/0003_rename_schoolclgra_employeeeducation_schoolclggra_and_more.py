# Generated by Django 4.1.5 on 2024-04-21 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_employeeexperience_employeeeducation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='schoolclgra',
            new_name='schoolclggra',
        ),
        migrations.RenameField(
            model_name='employeeeducation',
            old_name='schoolclssc',
            new_name='schoolclgssc',
        ),
    ]
