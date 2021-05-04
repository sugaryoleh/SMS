from django.contrib import admin

from _auth.models import User, Role

admin.site.register(Role)
admin.site.register(User)
