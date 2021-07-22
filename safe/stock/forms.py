from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from . models import UserProfile


class AmountForm(forms.Form):
    amount = forms.FloatField(initial=200)


class DepositForm(forms.Form):
    amount = forms.FloatField(initial=200)


class WithdrawForm(forms.Form):
    amount = forms.FloatField()


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'email',
                  )


class EdiForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('secret_question', 'secret_answer', 'wallet')


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, initial='name')
    email = forms.EmailField(initial='email')
    phone = forms.CharField(initial='phone number')
    message = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "cols": 45}))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('secret_question', 'secret_answer', 'wallet', )




