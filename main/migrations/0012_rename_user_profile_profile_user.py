# Generated by Django 4.2.1 on 2023-08-16 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_user_profile_user_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_profile',
            new_name='user',
        ),
    ]
