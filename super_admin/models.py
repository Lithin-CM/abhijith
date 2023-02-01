from django.db import models
import uuid
import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.
user_type = (('super_admin', 'super_admin'),('admin', 'admin'),('employees', 'employees'))


class User(AbstractUser):                                       #Agent model is change in User
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=True)
    name = models.CharField(max_length=20,null=False)
    user_type = models.CharField(max_length=10,choices=user_type,default='super_admin')

    is_active = models.BooleanField(default=True)
    info = models.JSONField(max_length=30,null=True,blank=True)
    created_at = models.DateTimeField("Created at",auto_now_add=True,blank=True)
    created_by = models.CharField(max_length=20,null=True,blank=True)
    updated_at = models.DateTimeField("Updated_at",auto_now_add=False,null=True,blank=True)
    updated_by = models.CharField(max_length=20,null=True,blank=True)
    deleted_at = models.DateTimeField("Delete at",auto_now=False,null=True,blank=True)
    deleted_by = models.CharField(max_length=20,null=True,blank=True)

    def _str_(self):
        return self.username