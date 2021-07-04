from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee


@receiver(post_save, sender=Employee)
def generate_id(sender, instance, created, **kwargs):
    '''function to generate employee id if created user_type is equal to employee'''

    if created:
        user_id = instance.id

        if instance.emp_role == 'hr':
            instance.emp_id = f'H-{user_id}'
            # setting user id to employee id with based on employee role.

        elif instance.emp_role == 'developer':
            instance.emp_id = f'D-{user_id}'

        elif instance.emp_role == 'manager':
            instance.emp_id = f'M-{user_id}'

        elif instance.emp_role == 'tester':
            instance.emp_id = f'T-{user_id}'

        instance.save()