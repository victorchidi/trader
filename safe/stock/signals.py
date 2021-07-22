from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from .models import Dashboard, UserProfile
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string

def dashboard_profile(sender, instance, created, **kwargs):
    if created:
        Dashboard.objects.create(user=instance)


post_save.connect(dashboard_profile, sender=User)


#@receiver(pre_save, sender=Car)
#def pre_save_create_code(sender, instance, **kwargs):
 #   if instance.code == "":
  #      instance.code = str(uuid.uuid4().replace('-', '').upper()[:10])

   # obj = Buyer.objects.get(user=instance.buyer)
    #obj.from_signal = True
    #obj.save()

    #post save
  #  @receiver(post_save, sender=Car)
   # def post_save_create_code(sender, instance, created, **kwargs):
    #    if instance.code == "":
     #       instance.code = str(uuid.uuid4().replace('-', '').upper()[:10])
      #      instance.save()

       # obj = Buyer.objects.get(user=instance.buyer)
        #obj.from_signal = True
        #obj.save()

@receiver(pre_save, sender=Dashboard)
def deposit_create(sender, instance, **kwargs):
    if instance.confirmed_deposit <= instance.balance:
        active = instance.balance - instance.confirmed_deposit
        instance.balance = active
        if instance.confirmed_deposit >= 15.0:
            total = instance.total_deposit + instance.confirmed_deposit
            instance.total_deposit = total
            if instance.confirmed_deposit >= 200 and instance.confirmed_deposit <= 1999:
                profit = instance.confirmed_deposit * (1.3 / 100)
                instance.profit = profit
            elif instance.confirmed_deposit >= 2000 and instance.confirmed_deposit <= 9999:
                profit = instance.confirmed_deposit * (1.5 / 100)
                instance.profit = profit
            elif instance.confirmed_deposit >= 10000 and instance.confirmed_deposit <= 29999:
                profit = instance.confirmed_deposit * (1.7 / 100)
                instance.profit = profit
            elif instance.confirmed_deposit >= 30000 and instance.confirmed_deposit <= 49999:
                profit = instance.confirmed_deposit * (2 / 100)
                instance.profit = profit
            elif instance.confirmed_deposit >= 50000 and instance.confirmed_deposit <= 99999:
                profit = instance.confirmed_deposit * (3 / 100)
                instance.profit = profit
            elif instance.confirmed_deposit >= 100000 and instance.confirmed_deposit <= 999999999:
                profit = instance.confirmed_deposit * (3.7 / 100)
                instance.profit = profit
            total_profit = instance.total_profit + instance.profit
            instance.total_profit = total_profit


@receiver(pre_save, sender=Dashboard)
def refer_create_bonus(sender, instance, **kwargs):
    if instance.referral == 5:
        instance.referral_bonus = instance.referral_bonus + 10
    elif instance.referral == 10:
        instance.referral_bonus = instance.referral_bonus + 10
    elif instance.referral == 15:
        instance.referral_bonus = instance.referral_bonus + 10
    elif instance.referral == 20:
        instance.referral_bonus = instance.referral_bonus + 10

@receiver(pre_save, sender=Dashboard)
def refer_confirm_withdraw(sender, instance, **kwargs):
    if instance.confirmed_withdraw >=15 and instance.confirmed_withdraw <= instance.balance:
        tot = instance.total_withdraw + instance.confirmed_withdraw
        instance.total_withdraw = tot
        tome = instance.balance - instance.confirmed_withdraw
        instance.balance = tome

@receiver(pre_save, sender=Dashboard)
def refer_create_bonus(sender, instance, **kwargs):
    if instance.confirmed_withdraw >= 10:
        obj = Dashboard.objects.filter(user=instance.user)[0]
        salt = obj.user.email
        name = obj.user.username
        amount = instance.confirmed_withdraw
        address = obj.user.userprofile

        context = {'name': name, 'amount': amount, 'address': address}
        subject = 'Your account has been credited'
        send_mail(
            subject,
            render_to_string('stock/withdraw_email.txt', context),
            'admin@acurainvestors.com',
            [salt],
        )
