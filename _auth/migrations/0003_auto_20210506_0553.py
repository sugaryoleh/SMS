# Generated by Django 3.1.7 on 2021-05-06 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('_auth', '0002_auto_20210506_0533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='roleId',
            new_name='role',
        ),
    ]
