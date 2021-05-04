from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import *

from _auth.models import User


class Post(models.Model):
    postId = AutoField(primary_key=True)
    name = CharField(max_length=20, null=False)
    salary = PositiveIntegerField(null=False)

class Employee(models.Model):
    employeeId = AutoField(primary_key=True)
    postId = ForeignKey(Post, on_delete=PROTECT, null=False)
    userId = ForeignKey(User, on_delete=PROTECT, null=True)
    hireDate = DateField(null=False)

class Address(models.Model):
    addressId = AutoField(primary_key=True)
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

class TreatmentCourse(models.Model):
    tcId = AutoField(primary_key=True)
    name = CharField(max_length=40, null=False)
    price = PositiveIntegerField(null=False, default=0)

class CustomerInfo(models.Model):
    customerInfoId = AutoField(primary_key=True)
    firstName = CharField(max_length=25, null=False)
    secondName = CharField(max_length=25, null=False)
    email = CharField(max_length=320, null=True)
    phone = CharField(max_length=15, null=False)
    visitsCnt = SmallIntegerField(null=False, default=0)

class Booking(models.Model):
    bookingId = AutoField(primary_key=True)
    roomId = ForeignKey(Room, on_delete=PROTECT, null=False)
    checkIn = DateField(null=False)
    checkOut = DateField(null=False)
    addedBy = ForeignKey(Employee, on_delete=SET_DEFAULT, default=1, null=False)

class Customer(models.Model):
    customerId = AutoField(primary_key=True)
    customerInfoId = ForeignKey(CustomerInfo, on_delete=CASCADE, null=False)
    bookingId = ForeignKey(Booking, on_delete=CASCADE, null=False)
    tcId = ForeignKey(TreatmentCourse, on_delete=SET_NULL, null=True)






