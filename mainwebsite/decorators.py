from django.http import HttpResponse
from django.shortcuts import redirect

from .models import *

def unauthenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('userdashboard')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            
            group=None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return redirect('/')
        return wrapper
    return decorator


def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        
        group=None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'members':
            return redirect('userdashboard')
        
        if group == 'admin':
            return view_func(request,*args,**kwargs)
        else:
            return redirect('unauthorized')
              
    return wrapper
