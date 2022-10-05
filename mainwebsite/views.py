from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView,ListView
from django.contrib.auth.decorators import login_required
from .decorators import admin_only, unauthenticated_user,allowed_users
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ForecasterPredictForm,MyUserCreationForm,UserProfileForm,StakeForm
from .models import*
from pages.models import *
from django.utils.decorators import method_decorator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .tokens import account_activation_token
# Create your views here.
#Home
class Home(TemplateView):
    template_name = 'mainwebsite/index.html'
    
#Static Pages
class AboutUs(TemplateView):
    template_name = 'mainwebsite/about.html'

# class Blog(TemplateView):
#     template_name = 'mainwebsite/blog.html'
    
class ContactUs(TemplateView):
    template_name = 'mainwebsite/contact.html'

class Faq(TemplateView):
    template_name = 'mainwebsite/faq.html'
    
class TermsAndConditions(TemplateView):
    template_name = 'mainwebsite/terms-conditions.html'
    
class PrivacyPolicy(TemplateView):
    template_name = 'mainwebsite/policy.html'
    
class HowToPlay(TemplateView):
    template_name = 'mainwebsite/how-to-play.html'
    
#Gameplay Page
    
class StakeLottery(TemplateView):
    template_name = 'mainwebsite/games.html'

    
class ForeCasters(TemplateView):
    template_name = 'mainwebsite/forecasters.html'
    
    

class forecastersboard(TemplateView):
    template_name = 'mainwebsite/forecasters-board.html'
 
    
class GameHistory(TemplateView):
    template_name = 'mainwebsite/lottery-history.html'

class RegisterForecaster(TemplateView):
    template_name = 'mainwebsite/register-forecaster.html'
    
class AccountSetting(TemplateView):
    template_name = 'mainwebsite/profile.html'

class Security(TemplateView):
    template_name = 'mainwebsite/change-pass.html'
    
#AUTH   
@ unauthenticated_user 
def signupPage(request):

    # if request.user.is_authenticated:
    #     return redirect('account:dashboard')

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email =form.cleaned_data['email']
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('mainwebsite/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully and activation sent')
    else:
        form =MyUserCreationForm()
    return render(request, 'mainwebsite/sign-up.html', {'form': form})


def account_activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('userdashboard')
    else:
        return render(request, 'mainwebsite/activation_invalid.html')
    
# User login page
@ unauthenticated_user  
def signinPage(request):
    if request.method=='POST':
        username =request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('userdashboard')
        else:
            messages.error(request, 'Username OR Password does not exit')    
    context={}
    return render(request, 'mainwebsite/sign-in.html', context)


def logoutUser(request):
    logout(request)
    return redirect('signin')


#USER DASHBOARD
@login_required(login_url='signin') 
# @allowed_users(allowed_roles=['members'])
def user_Dashboard(request):
    context ={}
    return render(request, 'mainwebsite/userdashboard.html', context)

@login_required(login_url='signin') 
# @allowed_users(allowed_roles=['members'])
def accountSetting(request):
    userprofile=request.user.userprofile
    form=UserProfileForm(instance=userprofile)
    if request.method=='POST':
        form=UserProfileForm(request.POST,request.FILES,instance=userprofile)
        if form.is_valid():
            form.save() 
    context ={'form':form}
    return render(request, 'mainwebsite/profile.html', context)


@login_required(login_url='signin') 
# @allowed_users(allowed_roles=['admin','members'])
def stakelog(request):
    Stakehistory =Stake.objects.all()
    context ={'Stakehistory':Stakehistory}
    return render(request, 'mainwebsite/stake-history.html', context)



@login_required(login_url='signin') 
# @allowed_users(allowed_roles=['admin','members'])
def deposit(request):
    context ={}
    return render(request, 'mainwebsite/deposit-log.html', context)

@login_required(login_url='signin') 
# @allowed_users(allowed_roles=['admin','members'])
def withdrawal(request):
    context ={}
    return render(request, 'mainwebsite/withdraw-log.html', context)

@login_required(login_url='signin') 
# @allowed_users(allowed_roles=['admin','members'])
def transaction(request):
    context ={}
    return render(request, 'mainwebsite/transaction.html', context)

@login_required(login_url='signin') 
# @allowed_users(allowed_roles=['admin','members'])
def forecastersboard(request):
    prediction=ForecasterPrediction.objects.all()
    
    form=ForecasterPredictForm()
    if request.method=='POST':
        form=ForecasterPredictForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
    
    context ={'form':form,
              'prediction':prediction,
              }
    return render(request, 'mainwebsite/forecasters-board.html', context)

@login_required(login_url='payments-log') 
# @allowed_users(allowed_roles=['admin','members'])
def paymentslog(request):
    context ={}
    return render(request, 'mainwebsite/payments-log.html', context)

@login_required(login_url='payments-log') 
# @allowed_users(allowed_roles=['admin','members'])
def forecastersubscribers(request):
    context ={}
    return render(request, 'mainwebsite/subscribers-forecasters.html', context)

@login_required(login_url='payments-log') 
# @allowed_users(allowed_roles=['admin','members'])
def forecastersubscribed(request):
    prediction=ForecasterPrediction.objects.all()
    

    context ={'prediction':prediction}
    return render(request, 'mainwebsite/subscribed-forecasters.html', context)



#Gameplay Page
@login_required(login_url='signin') 
# @allowed_users(allowed_roles=['admin','members'])
def game_details(request):
    
    draw=AddDraw.objects.all()
    
    form=StakeForm()
    if request.method =='POST':
        form=StakeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('stakehistory')
            
    context ={'form':form,'draw':draw}
    return render(request, 'mainwebsite/game-details.html', context)


@login_required(login_url='signin') 
# @allowed_users(allowed_roles=['admin','members'])
def stakelog(request):
    Stakehistory =Stake.objects.all()
    context ={'Stakehistory':Stakehistory}
    return render(request, 'mainwebsite/stake-history.html', context)

def lotteryResults(request):
    Results=AddWinDraw.objects.all()
    return render(request,'mainwebsite/results.html', {'Results':Results})

#Blog
def blog(request):
    blogs=Blog.objects.all()
    context ={'blogs':blogs}
    return render(request, 'mainwebsite/blog.html', context)


@login_required(login_url='signin') 
def blogdetail(request,pk):
    blog=get_object_or_404(Blog,id=pk)
    context ={'blog':blog}
    return render(request, 'mainwebsite/blog-details.html', context)