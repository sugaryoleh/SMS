# Generated by Django 3.1.7 on 2021-05-04 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=56)),
                ('state', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=85)),
                ('street', models.CharField(max_length=85)),
                ('buildingNum', models.PositiveIntegerField()),
                ('buildingCorpse', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('salary', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomPlacesType',
            fields=[
                ('placesCnt', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('roomTypeId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sanatorium',
            fields=[
                ('sanatoriumId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('addressId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_app.address')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomId', models.AutoField(primary_key=True, serialize=False)),
                ('roomPlacesTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_app.roomplacestype')),
                ('roomType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_app.roomtype')),
                ('sanatoriumId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_app.sanatorium')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeId', models.AutoField(primary_key=True, serialize=False)),
                ('hireDate', models.DateField()),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms_app.post')),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
