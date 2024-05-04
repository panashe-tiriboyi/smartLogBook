from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import Group
import uuid

#Employee for (Regular, Emplyee) Model with fields (id card_id name surname gender phoneNumber address post)
class Employee(AbstractUser, PermissionsMixin):

    # Add your custom fields here
    card_id = models.CharField(max_length=20)

        # unique groups for security and regular employees, because employees doesn't have to login by password

    gender = models.CharField(max_length=10)
    nationalID = models.CharField(max_length=20)
    
    phoneNumber = models.CharField(max_length=20)
    address = models.TextField()
    post = models.CharField(max_length=50)    

    # Custom field for employee type
    EMPLOYEE_TYPE_CHOICES = [
        ('Regular', 'Regular'),
        ('Employee', 'Employee'),
    ]

    employee_type = models.CharField(
        max_length=10,
        choices=EMPLOYEE_TYPE_CHOICES,
        default='Regular',
    )    

    def __str__(self):
        return (self.card_id)
    

    
# class EmployeeGroups(Group):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_groups')



#Attendance_Record Model with fields (id status entrancetime exiy_time)
class Attendance_Record(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20)
    entrance_time = models.DateTimeField()
    exit_time = models.DateTimeField()

    def __str__(self):
        return f"Attendance Record {self.id}"

