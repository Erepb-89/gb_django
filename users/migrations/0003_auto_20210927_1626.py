# Generated by Django 3.2.6 on 2021-09-27 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
