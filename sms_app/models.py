from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import *

from _auth.models import User
from sms_app.constraints import SANATORIUM_NAME_LENGTH

#TODO: add __str__, etrieve_meta, retrieve_filed_names, retrieve_fields
#TODO: rename methods


class CustomModel(models.Model):
    def __init__(self, *args, **kwargs):
        super.__init__(self, *args, **kwargs)
        self.dict = dict(zip(self.retrieve_field_names(), self.retrieve_field_values()))
        self.customer_dict = dict(zip(self.retrieve_customer_field_names(), self.retrieve_customer_field_values()))

    @staticmethod
    def retrieve_field_names():
        return ()
    def retrieve_field_values(self):
        return ()
    @staticmethod
    def retrieve_customer_field_names():
        return ()
    def retrieve_customer_field_values(self):
        return ()

class Post(models.Model, CustomModel):
    postId = AutoField(primary_key=True)
    name = CharField(max_length=20, null=False)
    salary = PositiveIntegerField(null=False)

    def __str__(self):
        return self.name

    @staticmethod
    def retrieve_customer_field_names():
        return ('Name', 'Salary')

    def retrieve_field_values(self):
        return (self.name, self.salary)

    @staticmethod
    def retrieve_field_names():
        return ('name', 'salary')


class Employee(models.Model, CustomModel):
    employeeId = AutoField(primary_key=True)
    post = ForeignKey(Post, on_delete=PROTECT, null=False)
    user = ForeignKey(User, on_delete=PROTECT, null=True)
    hireDate = DateField(null=False)

class Address(models.Model, CustomModel):
    addressId = AutoField(primary_key=True)
    country = CharField(max_length=56, null=False)
    state = CharField(max_length=30, null=False)
    city = CharField(max_length=85, null=False)
    street = CharField(max_length=85, null=False)
    buildingNum = PositiveIntegerField(null=False)
    buildingCorpse = CharField(max_length=1, null=False)

    def __getattr__(self, item):

    def __str__(self):
        return str(self.buildingNum) + self.buildingCorpse + ' ' + self.street  + ', ' + self.city + ', ' + self.state\
               + ', ' + self.country

    @staticmethod
    def retrieve_customer_field_names():
        return ('Country', 'State', 'City', 'Street', 'Building')

    def retrieve_field_values(self):
        return (self.country, self.state, self.city, self.street, str(self.buildingNum)+self.buildingCorpse)

    @staticmethod
    def retrieve_field_names():
        return ('country', 'state', 'city', 'street', 'buildingNum', 'buildingCorpse')


class Sanatorium(models.Model,CustomModel):
    sanatoriumId = AutoField(primary_key=True)
    address = ForeignKey(Address, on_delete=CASCADE, null=False)
    name = CharField(max_length=SANATORIUM_NAME_LENGTH, null=False)

    def __str__(self):
        return self.name

    @staticmethod
    def retrieve_customer_field_names():
        return ('Name', 'Address')

    def retrieve_field_values(self):
        return (self.name, str(self.address))

    @staticmethod
    def retrieve_field_names():
        return ('name', 'address_id')


class RoomType(models.Model, CustomModel):
    roomTypeId = AutoField(primary_key=True)
    name = CharField(max_length=20, null=False)
    description = CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def retrieve_customer_field_names():
        return ('Name', 'Description')

    def retrieve_field_values(self):
        return (self.name, self.description)

    @staticmethod
    def retrieve_field_names():
        return ('name', 'description')

class RoomPlacesType(models.Model, CustomModel):
    placesCnt = SmallIntegerField(primary_key=True, null=False)
    name = CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

    @staticmethod
    def retrieve_customer_field_names():
        return ('Places count', 'Name')

    def retrieve_field_values(self):
        return (self.placesCnt, self.name)

    @staticmethod
    def retrieve_field_names():
        return ('placesCnt', 'name')


class Room(models.Model, CustomModel):
    roomId = AutoField(primary_key=True)
    sanatorium = ForeignKey(Sanatorium, on_delete=CASCADE, null=False)
    roomNumber = SmallIntegerField(null=False)
    roomType = ForeignKey(RoomType, on_delete=CASCADE, null=False)
    roomPlacesType = ForeignKey(RoomPlacesType, on_delete=CASCADE, null=False)

    def __str__(self):
        return '#'+str(self.roomNumber) + ', ' + self.roomType.name + ', ' + self.roomPlacesType.name

    @staticmethod
    def retrieve_customer_field_names():
        return ('#', 'Type', 'Places')

    def retrieve_field_values(self):
        return (self.roomNumber, self.roomType.name, self.roomPlacesType.placesCnt)

    @staticmethod
    def retrieve_field_names():
        return ('sanatorium_id', 'roomNumber', 'roomType_id', 'roomPlacesType_id')


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
    room = ForeignKey(Room, on_delete=PROTECT, null=False)
    checkIn = DateField(null=False)
    checkOut = DateField(null=False)
    addedBy = ForeignKey(Employee, on_delete=SET_DEFAULT, default=1, null=False)


class Customer(models.Model):
    customerId = AutoField(primary_key=True)
    customerInfo = ForeignKey(CustomerInfo, on_delete=CASCADE, null=False)
    booking = ForeignKey(Booking, on_delete=CASCADE, null=False)
    tc = ForeignKey(TreatmentCourse, on_delete=SET_NULL, null=True)


def get_entries():
    return {
        'post':Post,
        'employee':Employee,
        'sanatorium':Sanatorium,
        'address': Address,
        'room_type':RoomType,
        'room_places_type':RoomPlacesType,
        'room':Room,
        'treatment_course':TreatmentCourse,
        'customer_info':CustomerInfo,
        'customer':Customer,
        'booking':Booking,
    }







