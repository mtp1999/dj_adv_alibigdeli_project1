# Generated by Django 3.2.22 on 2023-11-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAccount', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]