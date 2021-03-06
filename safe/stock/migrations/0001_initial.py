# Generated by Django 3.1.2 on 2021-07-21 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_question', models.CharField(blank=True, max_length=150, null=True)),
                ('secret_answer', models.CharField(blank=True, max_length=150, null=True)),
                ('wallet', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('bonus', models.FloatField(default=0.0)),
                ('profit', models.FloatField(default=0.0)),
                ('total_profit', models.FloatField(default=0.0)),
                ('plan', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('confirmed_date', models.DateTimeField(auto_now=True)),
                ('deposit', models.FloatField(default=0.0)),
                ('confirmed_deposit', models.FloatField(blank=True, default=0.0, null=True)),
                ('total_deposit', models.FloatField(blank=True, default=0.0, null=True)),
                ('withdraw', models.FloatField(default=0.0)),
                ('confirmed_withdraw', models.FloatField(blank=True, default=0.0, null=True)),
                ('total_withdraw', models.FloatField(blank=True, default=0.0, null=True)),
                ('referral', models.IntegerField(default=0)),
                ('referral_bonus', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
