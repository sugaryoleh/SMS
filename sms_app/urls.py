from django.urls import path

from sms_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('retrieve/<str:entry_name>/', views.retrieve_set, name='retrieve_set_view'),
    path('retrieve/<str:entry_name>/<int:entry_id>/', views.retrieve, name='retrieve_view'),
    path('create/<str:entry_name>/', views.create, name='create_view'),
    path('update/<str:entry_name>/<int:entry_id>/', views.update, name='update_view'),
    path('delete/<str:entry_name>/<int:entry_id>/', views.delete, name='delete_view'),
]
