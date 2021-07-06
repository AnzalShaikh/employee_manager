from django.shortcuts import render, redirect
from django.urls import reverse
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from employee.decorators import user_is_admin


@user_is_admin
def signup_view(requeset):
    '''function to create user'''

    form = CustomUserCreationForm(requeset.POST or None)
    if form.is_valid():
        instance = form.save()
        user_id = instance.id
        # user_id contains id of newly created user, which we will use to create employee.
        if form.cleaned_data['user_type'] == 'employee':
            # getting form data to check user type.
            return redirect(reverse('create_emp', kwargs={'pk': user_id}))
            # we want to create employee for newly created user so we are passing user id to employee form.
        return redirect('/')

    context = {'form': form}
    return render(requeset, 'registration/signup.html', context)