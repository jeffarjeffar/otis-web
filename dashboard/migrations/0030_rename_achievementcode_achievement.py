# Generated by Django 3.2.5 on 2021-08-04 23:23

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('roster', '0062_student_achievements'),
        ('dashboard', '0029_auto_20210804_1857'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AchievementCode',
            new_name='Achievement',
        ),
    ]
