from django.contrib import admin
from .models import Dashboard, UserProfile

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'plan', 'bonus', 'profit', 'confirmed_deposit', 'start_date',
                    'confirmed_date', 'withdraw', 'confirmed_withdraw', 'total_profit', 'referral')
    ordering = ('-start_date',)
    search_fields = ['user__username', 'user__email']
    list_filter = ('start_date', 'confirmed_date')


admin.site.register(Dashboard, AccountAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'wallet',)
    ordering = ('-id',)
    search_fields = ['user__username', 'user__email', ]


admin.site.register(UserProfile, UserAdmin)