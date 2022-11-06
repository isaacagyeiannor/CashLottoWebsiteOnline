from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import PwdResetForm,PwdResetConfirmForm

# app_name= 'mainwebsite'

urlpatterns = [
    #Home
    path(r'', views.Home.as_view(), name='home'),
    # path('', views.homePage, name="home"),
    #Blog
    # path('blog/', views.Blog.as_view(), name='blogs'),
    path('blogs/', views.blog, name="blogs"),
    path('blogs/<str:pk>/', views.blogdetail, name="blogdetails"),
    
    #Game Details
    # path('gamedetails/',views.GameDetails.as_view(), name='gamedetails'),
    # path('lotteryresults', views.LotteryResults.as_view(), name='lotteryresults'),
    path('stakelottery', views.StakeLottery.as_view(), name='stakelottery'),
    path('gamedetails/',views.game_details,name='gamedetails'),
    path('lotteryresults/',views.lotteryResults,name='lotteryresults'),
    
    #Static Pages
    path('aboutus', views.AboutUs.as_view(), name='aboutus'),
    path('contactus', views.ContactUs.as_view(), name='contactus'),
    path('faq', views.Faq.as_view(), name='faq'),
    path('termsandconditions', views.TermsAndConditions.as_view(), name='termsandconditions'),
    path('privacypolicy', views.PrivacyPolicy.as_view(), name='privacypolicy'),
    path('howtoplay', views.HowToPlay.as_view(), name='howtoplay'),
    
    #AUTH
    # path('login/', views.signinPage.as_view(), name="signin"),
    # path('signup/', views.signupPage.as_view(), name="signup"),
    path('forecasters', views.ForeCasters.as_view(), name='forecasters'),
    path('change-password', views.Security.as_view(), name='changepassword'),
    path('game-log', views.GameHistory.as_view(), name='gamelog'),
    path('registerforecaster/', views.RegisterForecaster.as_view(), name="registerforecaster"),
    path('login/', views.signinPage, name="signin"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signupPage, name="signup"),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
     #Password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='mainwebsite/password_reset.html',
                                                                success_url='password_reset_email_confirm',
                                                                email_template_name='mainwebsite/password_reset_email.html',
                                                                form_class=PwdResetForm),name='password-reset'),
    path('reset_password/password_reset_email_confirm', auth_views.PasswordResetDoneView.as_view(template_name='mainwebsite/password_reset_complete.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='mainwebsite/password_reset_confirm.html',
                                                                                                success_url='/password_reset_complete/', 
                                                                                                form_class=PwdResetConfirmForm),name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='mainwebsite/password_reset_complete.html'),name='password_reset_complete'),
    
    
    
    path('change-password', views.Security.as_view(), name='changepassword'),
    path('game-log', views.GameHistory.as_view(), name='gamelog'),
    
    
    #USER DASHBOARD
    path('user-dashboard/', views.user_Dashboard, name="userdashboard"),
    path('account-setting/', views.accountSetting, name="accountsetting"),
    path('stake-history/', views.stakelog, name="stakehistory"),
    path('deposit/', views.deposit, name="deposit"),
    path('withdrawal/', views.withdrawal, name="withdrawal"),
    path('transaction/', views.transaction, name="transaction"),
    path('forecasters-board/', views.forecastersboard, name="forecastersboard"),
    path('payments-log/', views.paymentslog, name="paymentslog"),
    path('forecaster-subscribers/', views.forecastersubscribers, name="forecastersubscribers"),
    path('suscribed-forecasters/', views.forecastersubscribed, name="subscribedforecasters"),
    
]
