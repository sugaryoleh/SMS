from django.urls import path, include

from _auth import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]