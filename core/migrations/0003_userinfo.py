# Generated by Django 3.2.3 on 2021-05-26 18:54

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210526_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=core.models.user_image_file_path)),
                ('age', models.IntegerField()),
                ('bio', models.CharField(max_length=400)),
                ('hobbies', models.CharField(max_length=255)),
                ('height', models.IntegerField()),
                ('gender', models.CharField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Transgender'), (4, 'non-binary')], default=1, max_length=255)),
                ('gender_preference', models.CharField(choices=[(1, 'Male'), (2, 'Female'), (3, 'All')], default=1, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]