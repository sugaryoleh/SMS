from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import *

# class PersonInfo(models.Model):
#     personInfoId = AutoField(primary_key=True)
#     firstName = CharField(max_length=25, blank=False)
#     secondName = CharField(max_length=25, blank=False)
#     email = CharField(max_length=320, blank=True)
#     phone = CharField(max_length=15, blank=False)

# class Meta(models.Model):
#     id = AutoField(primary_key=True)
#     createDate = DateField(blank=False)
#     updateDate = DateField(blank=False)
#     addedBy = OneToOneField(User, on_delete=CASCADE)
from _auth.models import User


class Post(models.Model):
    postId = AutoField(primary_key=True)
    name = CharField(max_length=20, null=False)
    salary = PositiveIntegerField(null=False)

class Employee(models.Model):
    employeeId = AutoField(primary_key=True)
    postId = ForeignKey(Post, on_delete=CASCADE, null=False)
    userId = ForeignKey(User, on_delete=CASCADE, null=True)
    hireDate = DateField(null=False)

class Address(models.Model):
    id = AutoField(primary_key=True)
    country = CharField(max_length=56, null=False)
    state = CharField(max_length=30, null=False)
    city = CharField(max_length=85, null=False)
    street = CharField(max_length=85, null=False)
    buildingNum = PositiveIntegerField(null=False)
    buildingCorpse = CharField(max_length=1, null=False)

class Sanatorium(models.Model):
    sanatoriumId = AutoField(primary_key=True)
    addressId = ForeignKey(Address, on_delete=CASCADE, null=False)
    name = CharField(max_length=50, null=False)

class RoomType(models.Model):
    roomTypeId = AutoField(primary_key=True)
    name = CharField(max_length=20, null=False)
    description = CharField(max_length=500, null=True)

class RoomPlacesType(models.Model):
    placesCnt = SmallIntegerField(primary_key=True, null=False)
    name = CharField(max_length=20, null=False)

class Room(models.Model):
    roomId = AutoField(primary_key=True)
    sanatoriumId = ForeignKey(Sanatorium, on_delete=CASCADE, null=False)
    roomType = ForeignKey(RoomType, on_delete=CASCADE, null=False)
    roomPlacesTypeId = ForeignKey(RoomPlacesType, on_delete=CASCADE, null=False)








