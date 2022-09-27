from django.urls import path
from . import views

urlpatterns = [
    #Home
    path('', views.Home.as_view(), name='home'),
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
    
    
    #USER DASHBOARD
    # path('user-dashboard/', views.user_Dashboard.as_view(), name="userdashboard"),
    # path('account-setting/', views.accountSetting.as_view(), name="accountsetting"),
    # path('stake-history/', views.stakelog.as_view(), name="stakehistory"),
    # path('deposit/', views.deposit.as_view(), name="deposit"),
    # path('withdrawal/', views.withdrawal.as_view(), name="withdrawal"),
    # path('transaction/', views.transaction.as_view(), name="transaction"),
    # path('forecasters-board/', views.forecastersboard.as_view(), name="forecastersboard"),
    # path('payments-log/', views.paymentslog.as_view(), name="paymentslog"),
    # path('forecaster-subscribers/', views.forecastersubscribers.as_view(), name="forecastersubscribers"),
    # path('suscribed-forecasters/', views.forecastersubscribed.as_view(), name="subscribedforecasters"),
    
    path('change-password', views.Security.as_view(), name='changepassword'),
    path('game-log', views.GameHistory.as_view(), name='gamelog'),
    
    
    # path('registerforecaster/', views.RegisterForecaster.as_view(), name="registerforecaster"),
    
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
