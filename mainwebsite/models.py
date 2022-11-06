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
    
    
class UserProfile(models.Model):
    user=models.OneToOneField(UserBase,blank=True,null=True,on_delete=models.CASCADE) 
    first_name=models.CharField(max_length=100, null=True,blank=True)
    last_name=models.CharField(max_length=100, null=True,blank=True)
    username = models.CharField(unique=True,max_length=200, null=True)
    email = models.EmailField( null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    address=models.CharField(max_length=100, null=True,blank=True)
    country=models.CharField(max_length=200, null=True,blank=True)
    phone_number=models.CharField(max_length=14, null=True,blank=True)
    code=models.CharField(max_length=10, null=True,blank=True)
    avatar = models.ImageField(null=True, blank=True,default="mediaflies/avatar.png")
    date_created=models.DateTimeField(auto_now_add=True, blank=True)  
    
    def __str__(self):
        return self.username     


class HistroyAbstract(models.Model):
    trans_id=models.CharField(max_length=100, null=True,blank=True)
    trans_type=models.CharField(max_length=100, null=True,blank=True)
    amount=models.FloatField(max_length=100, null=True,blank=True)
    
    
class DepositHistory(HistroyAbstract):
    date_created=models.DateTimeField(auto_now_add=True, blank=True) 
    
class withdrawHistory(HistroyAbstract):
    date_created=models.DateTimeField(auto_now_add=True, blank=True) 
    
class TransactionHistory(HistroyAbstract):
    date_created=models.DateTimeField(auto_now_add=True, blank=True) 
    
   
class Stake(models.Model):
    TYPE = (
        ('Monday Special','Monday Special'),
        ('Lucky Tuesday','Lucky Tuesday'),
        ('Lucky Wednesday','Lucky Tuesday'),
        ('Lucky Thursday','Lucky Tuesday'),
        ('Lucky Friday','Lucky Tuesday'),
    )
    
    PERM = (
        ('2 Direct ','2 Direct'),
        ('3 Direct','3 Direct'),
        ('Perm 2','Perm 2'),
        ('Perm 3','Perm 3'), 
    )
    
    game_type=models.CharField(max_length=100, null=True,blank=True,choices=TYPE)
    perm_type=models.CharField(max_length=100, null=True,blank=True,choices=PERM)
    first_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    second_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    third_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    fourth_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    fifth_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    price=models.FloatField(max_length=100, null=True,blank=True)
    winning_amount=models.FloatField(max_length=100, null=True,blank=True)
    payment=models.FloatField(max_length=100, null=True,blank=True)
    date_stake=models.DateTimeField(auto_now_add=True, blank=True) 
    
    

class ForecasterPrediction(models.Model):
    TYPE = (
        ('Monday Special','Monday Special'),
        ('Lucky Tuesday','Lucky Tuesday'),
        ('Mid Week','Mid Week'),
        ('Fortune Thursday','Fortune Thursday'),
        ('Friday Bonaza','Friday Bonaza'),
        ('National Weekly Lotto','National Weekly Lotto'),
        ('Sunday Aseda','Sunday Aseda'),
    )
    draw_type=models.CharField(max_length=100, null=True,blank=True,choices=TYPE,default="")
    date_select= models.CharField(max_length=50,default="") 
    first_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    second_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    third_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    fourth_number=models.PositiveIntegerField(blank=True,null=True,default="",validators=[less_than])
    fifth_number=models.PositiveIntegerField(blank=True,default="",validators=[less_than])
    date_created=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    win_draw = models.ForeignKey(AddWinDraw, on_delete=models.CASCADE,blank=True,null=True,default="") 