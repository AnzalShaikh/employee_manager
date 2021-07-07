from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeCreateForm, EmployeeChangeForm, UploadForm
from accounts.forms import CustomUserChangeForm
from .decorators import user_is_admin, user_or_admin
import csv

User = get_user_model()


@login_required
def home_view(request):
    '''function view for home view'''
    print(request.user.user_type)

    return render(request, 'employee/home.html')


@user_is_admin
def emp_create_view(request, pk):
    '''function view to create employee'''

    user = User.objects.get(id=pk)
    # getting newly created user id for which we want to create employee.
    form = EmployeeCreateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = user
        # joining employee user and created user, as we define in one to one field.
        instance.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'employee/emp_create.html', context)


@login_required
def emp_list_view(request):
    '''function view for employees list view'''

    emp_list = Employee.objects.all()

    context = {'emp_list': emp_list}
    return render(request, 'employee/emp_list.html', context)


# put all decorator in this order.
# first it verify login auth.
# then user or admin.
@user_or_admin
@login_required
def emp_detail_view(request, pk):
    '''function view for employee detail view'''

    emp = Employee.objects.get(id=pk)

    context = {'emp': emp}
    return render(request, 'employee/emp_detail.html', context)


@user_or_admin
@login_required
def emp_update_view(request, pk):
    '''function view to update employee details'''

    emp = Employee.objects.get(id=pk)
    user_form = CustomUserChangeForm(request.POST or None, instance=emp.user)
    emp_form = EmployeeChangeForm(request.POST or None, instance=emp)
    if user_form.is_valid() and emp_form.is_valid():
        user_form.save()
        emp_form.save()
        return redirect(reverse('detail_emp', kwargs={'pk': emp.id}))

    context = {'user_form': user_form, 'emp_form': emp_form}
    return render(request, 'employee/emp_update.html', context)


@user_is_admin
@login_required
def emp_delete_view(request, pk):
    '''function view to delete employee'''

    emp = get_object_or_404(Employee, id=pk)
    if request.method == 'POST':
        emp.user.delete()
        # deleting user of emplyee model, this will also delete employee.
        return redirect('list_emp')

    context = {'emp': emp}
    return render(request, 'employee/emp_delete.html', context)


@user_is_admin
@login_required
def emp_dataupload_view(request):
    '''function view to upload csv file'''

    form = UploadForm(data=request.POST or None, files=request.FILES)
    if form.is_valid():
        file = request.FILES['file']

        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        for row in reader:
            create_emp(row)
        return redirect('list_emp')

    context = {'form': form}
    return render(request, 'employee/upload_form.html', context)


def create_emp(data):
    user = User.objects.create_user(username=data['username'],
                                    email=data['email'],
                                    user_type=data['user_type'],
                                    password=data['password'])

    user.save()
    if user:
        emp = Employee.objects.create(
            emp_name=data['emp_name'],
            emp_role=data['emp_role'],
            emp_salary=data['emp_salary'],
            emp_joinied_date=data['emp_joinied_date'],
            emp_education=data['emp_education'],
            emp_age=data['emp_age'],
            emp_gender=data['emp_gender'],
            emp_contact=data['emp_contact'],
        )

    emp.user = user
    emp.save()
