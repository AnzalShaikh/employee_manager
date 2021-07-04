from django.urls import path
from .views import home_view, emp_create_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create/<int:pk>', emp_create_view, name='create_emp'),
    # user id(pk) is passed when we redirect reverse the user to employee form.
]