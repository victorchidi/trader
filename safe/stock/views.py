from django.shortcuts import render, redirect
from .forms import SignUpForm, AmountForm, EditProfileForm, DepositForm, \
    UserProfileForm, WithdrawForm, EdiForm, ContactForm
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from .models import Dashboard, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'stock/index2.html', {})


def about(request):
    return render(request, 'stock/about.html', {})


def policy(request):
    return render(request, 'stock/policy.html', {})


def contact(request):
    if request.method == 'GET':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')
            send_mail(
                name,
                message,
                email,
                ['admin@asset-trade.biz', 'victorotuson@gmail.com']
            )
            return redirect('/')
    form = ContactForm()
    return render(request, 'stock/contact.html', {'form': form})


def crypto(request):
    return render(request, 'stock/packages.html', {})


def gold(request):
    return render(request, 'stock/gold.html', {})


def escrow(request):
    return render(request, 'stock/escrow.html', {})


def forex(request):
    return render(request, 'stock/forex.html', {})


def carbon(request):
    return render(request, 'stock/carbon.html', {})


def real_estate(request):
    return render(request, 'stock/real-estate.html', {})


@login_required
def dashboard(request):
    son = Dashboard.objects.filter(user=request.user).order_by('-start_date')[0]
    return render(request, 'stock/wallet.html', {'son': son})


@login_required
def investment(request):
    correct = Dashboard.objects.filter(user=request.user).order_by('-start_date')[0]
    ac = Dashboard.objects.filter(user=request.user).order_by('-id')[0]
    if request.method == "POST":
        form = DepositForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            if amount <= ac.balance:
                if amount >= 200 and amount <= 1999:
                    tro = amount * (1.3 / 100)
                    Dashboard.objects.create(user=request.user,
                                             bonus=ac.bonus,
                                             balance=ac.balance,
                                             profit=tro,
                                             total_profit=ac.total_profit,
                                             plan='STARTER',
                                             confirmed_deposit=amount,
                                             total_deposit=ac.total_deposit,
                                             withdraw=0.0,
                                             confirmed_withdraw=0.0,
                                             total_withdraw=ac.total_withdraw,
                                             referral=ac.referral,
                                             referral_bonus=ac.referral_bonus
                                             )

                    messages.success(request, 'CONGRATULATIONS , '
                                              'You have Successfully Activated a New  STARTER Investment    !!!')

                    return redirect('dashboard')


                elif amount >= 2000 and amount <= 9999:
                    tro = amount * (1.5 / 100)
                    Dashboard.objects.create(user=request.user,
                                             bonus=ac.bonus,
                                             balance=ac.balance,
                                             profit=tro,
                                             total_profit=ac.total_profit,
                                             plan='PROFESSIONAL',
                                             confirmed_deposit=amount,
                                             total_deposit=ac.total_deposit,
                                             withdraw=0.0,
                                             confirmed_withdraw=0.0,
                                             total_withdraw=ac.total_withdraw,
                                             referral=ac.referral,
                                             referral_bonus=ac.referral_bonus
                                             )
                    messages.success(request, 'CONGRATULATIONS , '
                                              'You have Successfully Activated a New PROFESSIONAL Investment    !!!')

                    return redirect('dashboard')

                elif amount >= 10000 and amount <= 29999:
                    tro = amount * (1.7 / 100)
                    Dashboard.objects.create(user=request.user,
                                             bonus=ac.bonus,
                                             balance=ac.balance,
                                             profit=tro,
                                             total_profit=ac.total_profit,
                                             plan='CAPITALIST',
                                             confirmed_deposit=amount,
                                             total_deposit=ac.total_deposit,
                                             withdraw=0.0,
                                             confirmed_withdraw=0.0,
                                             total_withdraw=ac.total_withdraw,
                                             referral=ac.referral,
                                             referral_bonus=ac.referral_bonus
                                             )
                    messages.success(request, 'CONGRATULATIONS , '
                                              'You have Successfully Activated a New CAPITALIST Investment    !!!')

                    return redirect('dashboard')

                elif amount >= 30000 and amount <= 49999:
                    tro = amount * (2 / 100)
                    Dashboard.objects.create(user=request.user,
                                             bonus=ac.bonus,
                                             balance=ac.balance,
                                             profit=tro,
                                             total_profit=ac.total_profit,
                                             plan='LEVERAGE',
                                             confirmed_deposit=amount,
                                             total_deposit=ac.total_deposit,
                                             withdraw=0.0,
                                             confirmed_withdraw=0.0,
                                             total_withdraw=ac.total_withdraw,
                                             referral=ac.referral,
                                             referral_bonus=ac.referral_bonus
                                             )
                    messages.success(request, 'CONGRATULATIONS , '
                                              'You have Successfully Activated a New LEVERAGE Investment    !!!')

                    return redirect('dashboard')
                elif amount >= 50000 and amount <= 99999:
                    tro = amount * (3 / 100)
                    Dashboard.objects.create(user=request.user,
                                             bonus=ac.bonus,
                                             balance=ac.balance,
                                             profit=tro,
                                             total_profit=ac.total_profit,
                                             plan='MASTER',
                                             confirmed_deposit=amount,
                                             total_deposit=ac.total_deposit,
                                             withdraw=0.0,
                                             confirmed_withdraw=0.0,
                                             total_withdraw=ac.total_withdraw,
                                             referral=ac.referral,
                                             referral_bonus=ac.referral_bonus
                                             )
                    messages.success(request, 'CONGRATULATIONS , '
                                              'You have Successfully Activated a New MASTER Investment    !!!')

                    return redirect('dashboard')

                elif amount >= 100000 and amount <= 100000000:
                    tro = amount * (3.7 / 100)
                    Dashboard.objects.create(user=request.user,
                                             bonus=ac.bonus,
                                             balance=ac.balance,
                                             profit=tro,
                                             total_profit=ac.total_profit,
                                             plan='SHAREHOLDER',
                                             confirmed_deposit=amount,
                                             total_deposit=ac.total_deposit,
                                             withdraw=0.0,
                                             confirmed_withdraw=0.0,
                                             total_withdraw=ac.total_withdraw,
                                             referral=ac.referral,
                                             referral_bonus=ac.referral_bonus
                                             )
                    messages.success(request, 'CONGRATULATIONS , '
                                              'You have Successfully Activated a New SHAREHOLDER Investment    !!!')

                    return redirect('dashboard')

                else:
                    messages.error(request, 'Amount is less than the minimum investment amount ,'
                                            ' Fund your Account and try again  !!!')

            elif amount > ac.balance:
                messages.error(request, 'Insufficient Funds to perform this operation '
                                        ', Fund your Account and try again  !!!')

    form = DepositForm()
    return render(request, 'stock/investment.html', {'form': form})


@login_required
def fund(request):
    if request.method == "POST":
        form = AmountForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            if amount >= 200:
                return render(request, 'stock/fund-details.html', {'amount': amount})
            else:
                messages.error(request, ' Minimum amount to Fund Investment is $ 200   !!!')
    form = AmountForm()
    context = {'form': form}
    return render(request, 'stock/fund.html', context)


@login_required
def deposit_history(request):
    son = Dashboard.objects.filter(user=request.user).order_by('-start_date').exclude(confirmed_deposit=0.0)[:15]
    return render(request, 'stock/investment-history.html', {'son': son})


@login_required
def edit_account(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        prof = EdiForm(request.POST, instance=request.user.userprofile)
        if form.is_valid() and prof.is_valid():
            form.save()
            prof.save()
            messages.success(request, 'Your profile was successfully updated!!')
            return redirect('/edit/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        prof = EdiForm(instance=request.user.userprofile)
    context = {'form': form, 'prof': prof}
    return render(request, 'stock/profile.html', context)


@login_required
def referrals(request):
    son = Dashboard.objects.filter(user=request.user).order_by('-start_date')[0]
    return render(request, 'stock/Affiliate.html', {'son': son})


@login_required
def withdraw_history(request):
    son = Dashboard.objects.filter(user=request.user).order_by('-start_date').exclude(withdraw=0.0, confirmed_withdraw=0.0)[:15]
    hist = Dashboard.objects.filter(user=request.user).order_by('-id')
    return render(request, 'stock/withdraw-history.html', {'son': son})


@login_required
def withdraw(request):
    pan = UserProfile.objects.filter(user=request.user)
    draw = Dashboard.objects.filter(user=request.user).order_by('-id')[0]
    if request.method == 'POST':
        form = WithdrawForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            ac = draw.balance
            if amount >= 15.0 and amount <= ac:
                Dashboard.objects.create(user=request.user,
                                         bonus=draw.bonus,
                                         balance=draw.balance,
                                         plan=draw.plan,
                                         profit=0.0,
                                         total_profit=draw.total_profit,
                                         deposit=draw.confirmed_deposit,
                                         confirmed_deposit=0.0,
                                         total_deposit=draw.total_deposit,
                                         withdraw=amount,
                                         confirmed_withdraw=0.0,
                                         total_withdraw=draw.total_withdraw,
                                         referral=draw.referral,
                                         referral_bonus=draw.referral_bonus,
                                         )

                messages.success(request, 'CONGRATULATIONS , '
                                          'you have successfully placed a withdrawal , '
                                          'your withdrawal will be confirmed soon !!!')
            elif amount == 0.0 or amount < 15:
                messages.error(request, 'The amount you want withdraw is too small, please try a higher amount!!!')
            else:
                messages.error(request, 'You have insufficient Account Balance to withdraw from !!!')
    form = WithdrawForm()

    return render(request, 'stock/withdraw.html', {'draw': draw, 'form': form, 'pan': pan})


def entry(request, slug):
    res = render(request, 'stock/index.html')
    res.set_cookie('slug', slug)

    return res


def register(request):
    if request.user.is_authenticated:
        redirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            subject = 'Welcome to Asset-Trade'

            to = user.email
            tom = user.username
            first = user.first_name
            context = {'tom': tom, 'to': to}
            send_mail(
                subject,
                render_to_string('stock/email.txt', context),
                'admin@acurainvestors.com',
                [to],
                fail_silently=False
            )
            if 'entry' in request.COOKIES:
                UID = request.COOKIES['entry']
                pan = User.objects.get(username=UID)
                ac = Dashboard.objects.filter(user=pan).order_by('-id')[0]
                Dashboard.objects.create(user=pan, bonus=ac.bonus,
                                         balance=ac.balance,
                                         plan=ac.plan,
                                         profit=ac.profit,
                                         total_profit=ac.total_profit,
                                         deposit=ac.deposit,
                                         confirmed_deposit=ac.confirmed_deposit,
                                         total_deposit=ac.total_deposit,
                                         withdraw=ac.withdraw,
                                         confirmed_withdraw=ac.confirmed_withdraw,
                                         total_withdraw=ac.total_withdraw,
                                         referral=ac.referral + 1,
                                         referral_bonus=ac.referral_bonus,
                                         )
                salt = pan.email
                name = pan.username
                context = {'name': name, 'tom': tom, 'to': to, 'first': first}
                subject = 'You have a new direct signup on Asset Trade'
                send_mail(
                    subject,
                    render_to_string('stock/referral_email.html', context),
                    'admin@asset-trade.biz',
                    [salt],

                )

            return redirect('login')
    else:
        form = SignUpForm()
        profile_form = UserProfileForm()
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'stock/register.html', context)

