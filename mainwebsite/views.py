from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView,ListView
from django.contrib.auth.decorators import login_required
from .decorators import admin_only, unauthenticated_user,allowed_users
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import*
from pages.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.utils.decorators import method_decorator
from django.views.generic import FormView
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

class Blog(TemplateView):
    template_name = 'mainwebsite/blog.html'
    
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

class GameDetails(TemplateView):
    template_name = 'mainwebsite/game-details.html'

class LotteryResults(TemplateView):
    template_name = 'mainwebsite/results.html'
    
class ForeCasters(TemplateView):
    template_name = 'mainwebsite/forecasters.html'
    
    
#AUTH

class signinPage(TemplateView):
    template_name = 'mainwebsite/sign-in.html'
    
class signupPage(TemplateView):
    template_name = 'mainwebsite/sign-up.html'

#USER DASHBOARD
class user_Dashboard(TemplateView):
    template_name = 'mainwebsite/userdashboard.html'

class accountSetting(TemplateView):
    template_name = 'mainwebsite/profile.html'

class stakelog(TemplateView):
    template_name = 'mainwebsite/stake-history.html'
    
class deposit(TemplateView):
    template_name = 'mainwebsite/deposit-log.html'
    
class withdrawal(TemplateView):
    template_name = 'mainwebsite/withdraw-log.html'

class transaction(TemplateView):
    template_name = 'mainwebsite/transaction.html'

class forecastersboard(TemplateView):
    template_name = 'mainwebsite/forecasters-board.html'

class paymentslog(TemplateView):
    template_name = 'mainwebsite/payments-log.html'

class forecastersubscribers(TemplateView):
    template_name = 'mainwebsite/subscribers-forecasters.html'

class forecastersubscribed(TemplateView):
    template_name = 'mainwebsite/subscribed-forecasters.html'
    
class SubscribedForecasters(TemplateView):
    template_name = 'mainwebsite/subscribed-forecasters.html' 
    
class GameHistory(TemplateView):
    template_name = 'mainwebsite/lottery-history.html'

class RegisterForecaster(TemplateView):
    template_name = 'mainwebsite/register-forecaster.html'
    
class AccountSetting(TemplateView):
    template_name = 'mainwebsite/profile.html'

class Security(TemplateView):
    template_name = 'mainwebsite/change-pass.html'
    
    
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
            message = render_to_string('account_activation_email.html', {
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
