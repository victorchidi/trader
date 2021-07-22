from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Dashboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0, blank=True, null=True)
    bonus = models.FloatField(default=0.0)
    profit = models.FloatField(default=0.0)
    total_profit = models.FloatField(default=0.0)
    plan = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    confirmed_date = models.DateTimeField(auto_now=True)
    deposit = models.FloatField(default=0.0)
    confirmed_deposit = models.FloatField(default=0.0,  blank=True, null=True)
    total_deposit = models.FloatField(default=0.0,  blank=True, null=True)
    withdraw = models.FloatField(default=0.0)
    confirmed_withdraw = models.FloatField(default=0.0,  blank=True, null=True)
    total_withdraw = models.FloatField(default=0.0, blank=True, null=True)
    referral = models.IntegerField(default=0)
    referral_bonus = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user}   {self.plan}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secret_question = models.CharField(max_length=150, blank=True, null=True)
    secret_answer = models.CharField(max_length=150,  blank=True, null=True)
    wallet = models.CharField(max_length=150,  blank=True, null=True)

    def __str__(self):
        return f" {self.user}                {self.wallet}"

