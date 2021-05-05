from django.contrib import admin

from test_app.models import TestModel_1, TestModel_2

admin.site.register(TestModel_1)
admin.site.register(TestModel_2)
