# Generated by Django 3.0.6 on 2020-06-04 19:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0002_auto_20200604_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_model',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='is_following', to=settings.AUTH_USER_MODEL),
        ),
    ]
