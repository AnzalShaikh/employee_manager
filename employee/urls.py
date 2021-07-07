from django.urls import path
from .views import (
    home_view,
    emp_create_view,
    emp_list_view,
    emp_detail_view,
    emp_update_view,
    emp_delete_view,
    emp_dataupload_view,
    export_data,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('create/<int:pk>', emp_create_view, name='create_emp'),
    # user id(pk) is passed when we redirect reverse the user to employee form.
    path('list/', emp_list_view, name='list_emp'),
    path('detail/<int:pk>', emp_detail_view, name='detail_emp'),
    path('update/<int:pk>', emp_update_view, name='update_emp'),
    path('delete/<int:pk>', emp_delete_view, name='delete_emp'),
    path('upload/', emp_dataupload_view, name='upload_data'),
    path('export/', export_data, name='export_data'),
]