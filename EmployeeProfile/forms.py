from django import forms
from .models import *

class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model= EmployeeDetails
        fields='__all__'
