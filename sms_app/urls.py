from django.urls import path

from sms_app import views

urlpatterns = [
    path('', views.index, name='index')
]