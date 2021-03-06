# Generated by Django 3.1.7 on 2021-05-05 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms_app', '0007_employee_sanatorium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinfo',
            name='visitsCnt',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sanatorium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sms_app.sanatorium'),
        ),
    ]
