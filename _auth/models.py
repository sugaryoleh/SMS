from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import AutoField, CharField, ForeignKey, CASCADE


class Role(models.Model):
    roleId = AutoField(primary_key=True)
    name = CharField(max_length=20, blank=False, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = ForeignKey(Role, on_delete=CASCADE, default=1, null=False)
