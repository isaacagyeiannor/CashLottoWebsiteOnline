from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView

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