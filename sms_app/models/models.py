from datetime import timedelta

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.db.models import *

from sms_app.constraints import SANATORIUM_NAME_LENGTH

from sms_app.models.custom_models import CustomModel

#TODO: add __str__, retrieve_customer_filed_names, retrieve_customer_filed_values, retrieve_filed_names, retrieve_fields
#TODO: rename methods


class Post(models.Model, CustomModel):

    postId = AutoField(primary_key=True)
    name = CharField(max_length=20, null=False)
    salary = PositiveIntegerField(null=False)

    def __str__(self):
        return self.name

    @staticmethod
    def retrieve_field_names():
        return ('name', 'salary')

    def retrieve_field_values(self):
        return (self.name, self.salary)

    @staticmethod
    def retrieve_customer_field_names():
        return [field.capitalize() for field in Post.retrieve_field_names()]

    def retrieve_customer_field_values(self):
        return self.retrieve_field_values()



class Address(models.Model, CustomModel):
    addressId = AutoField(primary_key=True)
    country = CharField(max_length=56, null=False)
    state = CharField(max_length=30, null=False)
    city = CharField(max_length=85, null=False)
    street = CharField(max_length=85, null=False)
    buildingNum = PositiveIntegerField(null=False)
    buildingCorpse = CharField(max_length=1, null=True)

    def __str__(self):
        return str(self.buildingNum) + self.buildingCorpse + ' ' + self.street + ', ' + self.city + ', ' + self.state\
               + ', ' + self.country

    @staticmethod
    def retrieve_field_names():
        return ('country', 'state', 'city', 'street', 'buildingNum', 'buildingCorpse')

    def retrieve_field_values(self):
        return (self.country, self.state, self.city, self.street, self.buildingNum, self.buildingCorpse)

    @staticmethod
    def retrieve_customer_field_names():
        return ('Country', 'State', 'City', 'Street', 'Building')

    def retrieve_customer_field_values(self):
        return (self.country, self.state, self.city, self.street, str(self.buildingNum)+str(self.buildingCorpse))



class Sanatorium(models.Model,CustomModel):
    sanatoriumId = AutoField(primary_key=True)
    address = ForeignKey(Address, on_delete=CASCADE, null=False)
    name = CharField(max_length=SANATORIUM_NAME_LENGTH, null=False)

    def __str__(self):
        return self.name

    @staticmethod
    def retrieve_field_names():
        return ('name', 'address')

    def retrieve_field_values(self):
        return (self.name, str(self.address))

    @staticmethod
    def retrieve_customer_field_names():
        return [field.capitalize() for field in Sanatorium.retrieve_field_names()]

    def retrieve_customer_field_values(self):
        return self.retrieve_field_values()


class RoomType(models.Model, CustomModel):
    roomTypeId = AutoField(primary_key=True)
    name = CharField(max_length=20, null=False)
    description = CharField(max_length=500, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def retrieve_field_names():
        return ('name', 'description')

    def retrieve_field_values(self):
        return (self.name, self.description)

    @staticmethod
    def retrieve_customer_field_names():
        return [field.capitalize() for field in RoomType.retrieve_field_names()]

    def retrieve_customer_field_values(self):
        return self.retrieve_field_values()


class RoomPlacesType(models.Model, CustomModel):
    placesCnt = SmallIntegerField(primary_key=True, null=False)
    name = CharField(max_length=20, null=False)

    def __str__(self):
        return self.name

    @staticmethod
    def retrieve_field_names():
        return ('placesCnt', 'name')

    def retrieve_field_values(self):
        return (self.placesCnt, self.name)

    @staticmethod
    def retrieve_customer_field_names():
        return ('Places count', 'Name')

    def retrieve_customer_field_values(self):
        return self.retrieve_field_values()


class Room(models.Model, CustomModel):
    roomId = AutoField(primary_key=True)
    sanatorium = ForeignKey(Sanatorium, on_delete=CASCADE, null=False)
    roomNumber = SmallIntegerField(null=False)
    roomType = ForeignKey(RoomType, on_delete=CASCADE, null=False)
    roomPlacesType = ForeignKey(RoomPlacesType, on_delete=CASCADE, null=False)
    price = IntegerField(null=True, default=0)

    def save(self, *args, **kwargs):
        print(Room.objects.filter(sanatorium=self.sanatorium))
        if self.roomNumber in [room.roomNumber for room in Room.objects.filter(sanatorium=self.sanatorium)]:
            raise ValueError("Cannot be created! Room with {} exists!".format(self.roomNumber))
        super().save(self, *args, **kwargs)

    def __str__(self):
        return 'Room#'+str(self.roomNumber) + ', ' + self.sanatorium.name

    @staticmethod
    def retrieve_field_names():
        return ('sanatorium', 'roomNumber', 'roomType', 'roomPlacesType')

    def retrieve_field_values(self):
        return (self.roomNumber, self.roomType.name, self.roomPlacesType.name)

    @staticmethod
    def retrieve_customer_field_names():
        return ('Room#', 'Type', 'Places')

    def retrieve_customer_field_values(self):
        return (self.roomNumber, self.roomType.name, self.roomPlacesType.name)


class TreatmentCourse(models.Model, CustomModel):
    tcId = AutoField(primary_key=True)
    name = CharField(max_length=40, null=False)
    price = PositiveIntegerField(null=False, default=0)

    def __str__(self):
        return str(self.name) + '\t' + str(self.price)

    @staticmethod
    def retrieve_field_names():
        return ('name', 'price')

    def retrieve_field_values(self):
        return (self.name, self.price)

    @staticmethod
    def retrieve_customer_field_names():
        return [field.capitalize() for field in TreatmentCourse.retrieve_field_names()]

    def retrieve_customer_field_values(self):
        return (self.name, self.price)


class CustomerInfo(models.Model, CustomModel):
    customerInfoId = AutoField(primary_key=True)
    firstName = CharField(max_length=25, null=False)
    secondName = CharField(max_length=25, null=False)
    email = CharField(max_length=320, null=True)
    phone = CharField(max_length=15, null=False)
    visitsCnt = SmallIntegerField(null=False)

    def __str__(self):
        return str(self.firstName) + ' ' + str(self.secondName)

    @staticmethod
    def retrieve_field_names():
        return ('firstName', 'secondName', 'email', 'phone', 'visitsCnt')

    def retrieve_field_values(self):
        return (self.firstName, self.secondName, self.email, self.phone, self.visitsCnt)

    @staticmethod
    def retrieve_customer_field_names():
        return ('First name', 'Second name', 'E-mail', 'Phone', 'Visits')

    def retrieve_customer_field_values(self):
        return self.retrieve_field_values()


class Employee(models.Model, CustomModel):
    employeeId = AutoField(primary_key=True)
    post = ForeignKey(Post, on_delete=PROTECT, null=False)
    user = ForeignKey(User, on_delete=CASCADE, null=True)
    sanatorium = ForeignKey(Sanatorium, on_delete=PROTECT, null=False)
    hireDate = DateField(null=False)

    def __str__(self):
        return self.user.get_full_name()

    @staticmethod
    def retrieve_field_names():
        return ('name', 'post', 'sanatorium', 'hireDate')

    def retrieve_field_values(self):
        return (self.user.get_full_name(), self.post.name, self.sanatorium.name, self.hireDate)

    @staticmethod
    def retrieve_customer_field_names():
        return ('Name', 'Post', 'Sanatorium', 'Hire date')

    def retrieve_customer_field_values(self):
        return self.retrieve_field_values()

class Booking(models.Model, CustomModel):
    bookingId = AutoField(primary_key=True)
    room = ForeignKey(Room, on_delete=PROTECT, null=False)
    checkIn = DateField(null=False)
    checkOut = DateField(null=False)
    addedBy = ForeignKey(Employee, on_delete=SET_DEFAULT, null=False, default=1)
    payed = BooleanField(default=False, null=False)
    closed = BooleanField(default=False, null=False)

    def save(self, *args, **kwargs):
        if self.checkIn > self.checkOut:
            raise ValueError("Cannot be deleted! Check-out date must be later or equal check-in date!")
        super().save(*args, **kwargs)

    @staticmethod
    def retrieve_field_names():
        return ('room', 'checkIn', 'checkOut', 'addedBy', 'payed', 'closed')

    def retrieve_field_values(self):
        return (self.room, self.checkIn, self.checkOut, self.addedBy, self.payed, self.closed)

    @staticmethod
    def retrieve_customer_field_names():
        return ('Customers', 'Room', 'Check in', 'Check out', 'Added by', 'Payed', 'Closed')

    def retrieve_customer_field_values(self):
        customers = list(Customer.objects.filter(booking=self))
        customers = list(customer.customerInfo.firstName + ' ' + customer.customerInfo.secondName for customer in customers)
        customers = ', '.join(customers)
        payed = None
        closed = None
        if self.payed:
            payed='Yes'
        else:
            payed='No'
        if self.closed:
            closed='Yes'
        else:
            closed='No'
        return (customers, self.room, self.checkIn, self.checkOut, self.addedBy, payed, closed)

    def customer_dict(self):
        room_total = (self.checkOut - self.checkIn).days*self.room.price
        tc_total = sum([customer.tc.price for customer in Customer.objects.filter(booking=self)])
        names = list(self.retrieve_customer_field_names())
        names.append('Room total')
        names.append('Treatment course total')
        names.append('Customers')
        values = list(self.retrieve_field_values())
        values.append(room_total)
        values.append(tc_total)
        customers = list(Customer.objects.filter(booking=self))
        customers = list(customer.customerInfo.firstName+' '+customer.customerInfo.secondName for customer in customers)
        customers = ', '.join(customers)
        values.append(customers)
        return dict(zip(names, values))


class Customer(models.Model, CustomModel):
    customerId = AutoField(primary_key=True)
    customerInfo = ForeignKey(CustomerInfo, on_delete=CASCADE, null=False)
    booking = ForeignKey(Booking, on_delete=CASCADE, null=False)
    tc = ForeignKey(TreatmentCourse, on_delete=SET_NULL, null=True)
    sanatorium = ForeignKey(Sanatorium, on_delete=PROTECT, null=False, default=1)

    def save(self, *args, **kwargs):
        if len(Customer.objects.filter(booking=self.booking)) > self.booking.room.roomPlacesType.placesCnt:
            raise ValueError("Cannot be add customer! Room is full!")
        self.sanatorium = self.booking.room.sanatorium
        super().save(*args, **kwargs)

    @staticmethod
    def retrieve_field_names():
        return ('customerInfo', 'booking', 'treatmentCourse')

    def retrieve_field_values(self):
        return (self.customerInfo, self.booking, self.tc)

    @staticmethod
    def retrieve_customer_field_names():
        return ('Customer', 'Booking', 'Treatment course')

    def retrieve_customer_field_values(self):
        return self.retrieve_field_values()

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