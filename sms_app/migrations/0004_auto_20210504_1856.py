# Generated by Django 3.1.7 on 2021-05-04 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0003_auto_20210504_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='roomPlacesTypeId',
            new_name='roomPlacesType',
        ),
        migrations.AddField(
            model_name='room',
            name='roomNumber',
            field=models.SmallIntegerField(default=0),
        ),
    ]
