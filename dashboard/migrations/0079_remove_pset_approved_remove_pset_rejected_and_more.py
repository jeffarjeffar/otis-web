# Generated by Django 4.0.7 on 2022-09-26 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0078_auto_20220926_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pset',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='pset',
            name='rejected',
        ),
        migrations.RemoveField(
            model_name='pset',
            name='resubmitted',
        ),
    ]