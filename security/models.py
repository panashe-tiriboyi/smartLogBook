# from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
# from django.db import models
# from django.contrib.auth.models import Group

# class Security(AbstractUser, PermissionsMixin):
#     # name = models.CharField(max_length=100)
#     # surname = models.CharField(max_length=100)
#     gender = models.CharField(max_length=10)
#     phoneNumber = models.CharField(max_length=20)
#     address = models.TextField()
#     nationalID = models.CharField(max_length=20)
    
#     class Meta:
#             # Add the following lines to give unique related names
#             # Adjust as needed based on your project structure
#             unique_together = ['id']
#             id = 'SecurityGroups'
    



#     def __str__(self):
#         return f"{self.username} ({self.name} {self.surname})"


# Specify unique related names for reverse relations
# class SecurityGroups(Group):
#     security = models.ForeignKey(Security, on_delete=models.CASCADE, related_name='security_groups')



# -----------------------------------------------------------------------------------------------------------------------------------------
# meta
# -----------------------------------------------------------------------------------------------------------------------------------------

# class Meta:
#         # Add the following lines to give unique related names
#         # Adjust as needed based on your project structure
#         unique_together = ['id']
#         related_name = 'employee_groups'
    