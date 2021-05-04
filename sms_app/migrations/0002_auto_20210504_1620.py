# Generated by Django 3.1.7 on 2021-05-04 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sms_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bookingId', models.AutoField(primary_key=True, serialize=False)),
                ('checkIn', models.DateField()),
                ('checkOut', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('customerInfoId', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=25)),
                ('secondName', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=320, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('visitsCnt', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentCourse',
            fields=[
                ('tcId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('price', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sms_app.post'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerId', models.AutoField(primary_key=True, serialize=False)),
                ('bookingId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_app.booking')),
                ('customerInfoId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_app.customerinfo')),
                ('tcId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sms_app.treatmentcourse')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='addedBy',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='sms_app.employee'),
        ),
        migrations.AddField(
            model_name='booking',
            name='roomId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sms_app.room'),
        ),
    ]
