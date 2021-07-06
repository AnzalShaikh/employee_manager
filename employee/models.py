from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

User = get_user_model()

EMPLOYEE_ROLE = [('HR', 'hr'), ('Developer', 'developer'),
                 ('Tester', 'tester'), ('Manager', 'manager')]

GENDER = [('Male', 'male'), ('Female', 'female')]


class Employee(models.Model):
    '''class to create employee model'''

    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    emp_name = models.CharField(max_length=250)
    emp_id = models.CharField(max_length=20, null=True, blank=True)
    # null and blank is true beacause we are creating employee id through signals after creating emplyee.
    emp_role = models.CharField(max_length=250, choices=EMPLOYEE_ROLE)
    emp_salary = models.DecimalField(max_digits=8, decimal_places=2)
    emp_joinied_date = models.DateField(default=date.today())
    emp_education = models.CharField(max_length=250)
    emp_age = models.IntegerField()
    emp_gender = models.CharField(max_length=250, choices=GENDER)
    emp_contact = models.CharField(max_length=10)

    def __str__(self):
        return self.emp_name