from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'EmployeeProfile'

urlpatterns = [
    path('show_details/<int:id>',show_details,name='show_details'),
    path('', employee_list, name='employee_list'),
    path('add_details/', create_profile, name="create_profile"),
    path('delete/<int:id>', delete_profile, name='delete_profile'),
    path('edit/<int:id>', edit_profile, name="edit_profile"),

   
]                                                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                         