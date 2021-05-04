from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import *

# class PersonInfo(models.Model):
#     personInfoId = AutoField(primary_key=True)
#     firstName = CharField(max_length=25, blank=False)
#     secondName = CharField(max_length=25, blank=False)
#     email = CharField(max_length=320, blank=True)
#     phone = CharField(max_length=15, blank=False)


class Role(models.Model):
    roleId = AutoField(primary_key=True)
    name = CharField(max_length=20, blank=False)

class User(AbstractUser):
    roleId = ForeignKey(Role, on_delete=CASCADE, default=1)

class Meta(models.Model):
    id = AutoField(primary_key=True)
    createDate = DateField(blank=False)
    updateDate = DateField(blank=False)
    addedBy = OneToOneField(User, on_delete=CASCADE)

class Address(models.Model):
    id = AutoField(primary_key=True)
    country = CharField(max_length=56, blank=False)
    state = CharField(max_length=30, blank=False)
    city = CharField(max_length=85, blank=False)
    street = CharField(max_length=85, blank=False)
    buildingNum = PositiveIntegerField(blank=False)
    buildingCorpse = CharField(max_length=1, blank=False)
    

