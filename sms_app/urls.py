from django.urls import path

from sms_app import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('retrieve/<str:entry_name>/', views.retrieve_entry_set, name='retrieve_entry_set_view'),
    path('retrieve/<str:entry_name>/<int:id>', views.retrieve_entry, name='retrieve_entry_view'),
    path('create/<str:entry_name>/', views.create_entry, name='create_entry_view'),
]
