from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import AutoField, CharField, ForeignKey, CASCADE


class Role(models.Model):
    roleId = AutoField(primary_key=True)
    name = CharField(max_length=20, blank=False)

class User(AbstractUser):
    roleId = ForeignKey(Role, on_delete=CASCADE, default=1, null=False)
