# Generated by Django 3.1.7 on 2021-05-06 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sms_app', '0013_room_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='sanatorium',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='sms_app.sanatorium'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
