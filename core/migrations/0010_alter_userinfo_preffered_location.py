# Generated by Django 3.2.3 on 2021-05-31 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_userinfo_preffered_age_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='preffered_location',
            field=models.CharField(choices=[('AM', 'Assam'), ('BG', 'Bangalore'), ('DL', 'Delhi'), ('GZ', 'Ghaziabad'), ('GJ', 'Gujrat'), ('KL', 'Kerala'), ('MU', 'Mumbai'), ('ND', 'Noida'), ('PU', 'Pune'), ('TN', 'Tamil Nadu')], default='Goa', max_length=255),
        ),
    ]
