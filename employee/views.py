from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Employee
from .forms import EmployeeCreateForm

User = get_user_model()


def home_view(request):
    return render(request, 'employee/home.html')


def emp_create_view(request, pk):
    '''function to create employee'''

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