# Generated by Django 3.2.7 on 2021-09-10 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0044_alter_level_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemsuggestion',
            name='reason',
        ),
    ]