from django import forms
from sms_app.models.models import *

class BaseMeta:
    fields='__all__'


class PostCreateForm(forms.ModelForm):

    class Meta(BaseMeta):
        model = Post


class EmployeeCreateForm(forms.ModelForm):

    class Meta(BaseMeta):
        model = Employee


class AddressCreateForm(forms.ModelForm):

    class Meta(BaseMeta):
        model = Address


class SanatoriumCreateForm(forms.ModelForm):

    class Meta(BaseMeta):
        model = Sanatorium

class RoomTypeCreateForm(forms.ModelForm):

    class Meta(BaseMeta):
        model = RoomType


class RoomPlacesTypeCreateForm(forms.ModelForm):

    class Meta(BaseMeta):
        model = RoomPlacesType


class RoomCreateForm(forms.ModelForm):

    class Meta(BaseMeta):
        model = Room


def get_create_forms():
    return {
        'post':PostCreateForm,
        'employee':EmployeeCreateForm,
        'sanatorium':SanatoriumCreateForm,
        'address': AddressCreateForm,
        'room_type':RoomTypeCreateForm,
        'room_places_type':RoomPlacesTypeCreateForm,
        'room':RoomCreateForm,
        # 'treatment_course':TreatmentCourseCreateForm,
        # 'customer_info':CustomerInfoCourseCreateForm,
        # 'customer':CustomerCourseCreateForm,
        # 'booking':BookingCourseCreateForm,
    }
