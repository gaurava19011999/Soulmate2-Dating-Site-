# Generated by Django 3.2.3 on 2021-05-31 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_userinfo_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='location',
            field=models.CharField(choices=[('AM', 'Assam'), ('BG', 'Bangalore'), ('DL', 'Delhi'), ('GZ', 'Ghaziabad'), ('GJ', 'Gujrat'), ('KL', 'Kerala'), ('MU', 'Mumbai'), ('ND', 'Noida'), ('PU', 'Pune'), ('TN', 'Tamil Nadu')], default='AM', max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='preffered_age_group',
            field=models.CharField(choices=[('Y', 'Young'), ('O', 'Older'), ('O+', 'Old')], default='Y', max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='preffered_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('A', 'All')], default='M', max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='preffered_location',
            field=models.CharField(choices=[('AM', 'Assam'), ('BG', 'Bangalore'), ('DL', 'Delhi'), ('GZ', 'Ghaziabad'), ('GJ', 'Gujrat'), ('KL', 'Kerala'), ('MU', 'Mumbai'), ('ND', 'Noida'), ('PU', 'Pune'), ('TN', 'Tamil Nadu')], default='AM', max_length=255),
        ),
    ]