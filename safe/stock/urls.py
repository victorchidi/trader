from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('policy/', views.policy, name='policy'),
    path('contact/', views.contact, name='contact'),
    path('crypto/', views.crypto, name='crypto'),
    path('escrow/', views.escrow, name='escrow'),
    path('forex/', views.forex, name='forex'),
    path('carbon/', views.carbon, name='carbon'),
    path('gold/', views.gold, name='gold'),
    path('real-estate/', views.real_estate, name='real_estate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('fund/wallet/', views.fund, name='fund'),
    path('investment/', views.investment, name='investment'),
    path('investment/history/', views.deposit_history, name='deposit_history'),
    path('edit/profile/', views.edit_account, name='edit_profile'),
    path('referrals/', views.referrals, name='referrals'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('withdraw/history/', views.withdraw_history, name='withdraw_history'),
    path('referral/<str:slug>/', views.entry, name='referral'),
    path('register/', views.register, name='register'),
]