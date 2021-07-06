from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeCreateForm, EmployeeChangeForm
from accounts.forms import CustomUserChangeForm

User = get_user_model()


@login_required
def home_view(request):
    '''function view for home view'''

    return render(request, 'employee/home.html')


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


@login_required
def emp_detail_view(request, pk):
    '''function view for employee detail view'''

    emp = Employee.objects.get(id=pk)

    context = {'emp': emp}
    return render(request, 'employee/emp_detail.html', context)


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
