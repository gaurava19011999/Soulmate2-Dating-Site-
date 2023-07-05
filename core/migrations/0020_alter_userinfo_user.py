# Generated by Django 3.2.3 on 2021-06-29 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_userinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
