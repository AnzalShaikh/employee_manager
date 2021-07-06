from django.core.exceptions import PermissionDenied
from .models import Employee
from django.contrib.auth import get_user_model

User = get_user_model()


def user_is_admin(func):
    def wrap(request, *args, **kwargs):
        if request.user.user_type == 'admin':
            return func(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap


# put user is admin decorator on signup view, create employee view and delete view.


def user_or_admin(func):
    def wrap(request, *args, **kwargs):
        if request.user.user_type == 'admin':
            return func(request, *args, **kwargs)

        elif request.user.employee.id == kwargs['pk']:
            return func(request, *args, **kwargs)

        else:
            raise PermissionDenied

    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap


# put user or admin view on detail view and update view.