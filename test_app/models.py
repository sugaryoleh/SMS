from django.db import models
from django.db.models import AutoField, SET_NULL, ForeignKey


class TestModel_1(models.Model):
    id = AutoField(primary_key=True)

class TestModel_2(models.Model):
    id = AutoField(primary_key=True)
    fk = ForeignKey(TestModel_1, on_delete=SET_NULL, null=True)