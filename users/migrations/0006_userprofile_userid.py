# Generated by Django 3.2.6 on 2021-10-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211002_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='userid',
            field=models.CharField(blank=True, max_length=128, verbose_name='link'),
        ),
    ]
