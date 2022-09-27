from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from pages.models import *
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.



def less_than(value):
    if value > 90:
        raise ValidationError(
            _('%(value)s is greater than 90 '),
            params={'value': value},
        )


class UserBase(AbstractUser):
    name=models.CharField(max_length=100, null=True,blank=True)
    username = models.CharField(unique=True,max_length=200, null=True)
    email = models.EmailField( null=True,blank=True)
    country=models.CharField(max_length=200, null=True,blank=True)
    phone_number=models.CharField(max_length=14, null=True,blank=True)
    code=models.CharField(max_length=10, null=True,blank=True)