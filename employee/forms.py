from django import forms
from django.forms import ModelForm
from .models import Employee


class EmployeeCreateForm(ModelForm):
    class Meta:
        model = Employee
        fields = (
            'emp_name',
            'emp_role',
            'emp_salary',
            'emp_joinied_date',
            'emp_education',
            'emp_age',
            'emp_gender',
            'emp_contact',
        )


class EmployeeChangeForm(ModelForm):
    class Meta:
        model = Employee
        fields = (
            'emp_name',
            'emp_role',
            'emp_salary',
            'emp_education',
            'emp_age',
            'emp_gender',
            'emp_contact',
        )


class UploadForm(forms.Form):
    file = forms.FileField()