# Generated by Django 3.2.3 on 2021-05-26 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'Transgender'), ('NB', 'non-binary')], default=1, max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender_preference',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('A', 'All')], default=1, max_length=255),
        ),
    ]