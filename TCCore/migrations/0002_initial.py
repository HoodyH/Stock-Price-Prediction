# Generated by Django 4.0.3 on 2022-03-22 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TCWallet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TCCore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradingblock',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tradingblock',
            name='wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='TCWallet.wallet'),
        ),
    ]
