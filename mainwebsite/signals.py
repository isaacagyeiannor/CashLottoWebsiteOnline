from django.db.models.signals import post_save
from .models import UserProfile,UserBase
from django.contrib.auth.models import Group
from django.dispatch import receiver


def member_profile(sender,instance,created,**kwargs):
    if created:
        group, created = Group.objects.get_or_create(name='members')
        # group=Group.objects.get(name='members')
        instance.groups.add(group)
            
        UserProfile.objects.create(user=instance,
            username=instance.username,
            email=instance.email,
            phone_number=instance.phone_number,
            country=instance.country,
            )
        print('Profile Created')
        
post_save.connect(member_profile, sender=UserBase) 


# @receiver(post_save,sender=User)
# def created_member(sender,instance,created,**kwargs):
#     if created:
#         Membership.objects.create(user=instance)
#         print('member is created')
        
# # post_save.connect(created_member, sender=User)       

# @receiver(post_save,sender=User)     
def created_updated(sender,instance,created,**kwargs):
    if created==False:
        instance.userprofile.save()
        print('member is created')       
        
post_save.connect(created_updated, sender=UserBase)   