from django.db import models
from django.db.models import AutoField, SET_NULL, ForeignKey, IntegerField, OneToOneField


class TestModel_1(models.Model):
    id = AutoField(primary_key=True)
    v = IntegerField(default=0, null=False)

class TestModel_2(models.Model):
    id = AutoField(primary_key=True)
    fk = ForeignKey(TestModel_1, on_delete=SET_NULL, null=True)
    v = IntegerField(null=False, default=0)