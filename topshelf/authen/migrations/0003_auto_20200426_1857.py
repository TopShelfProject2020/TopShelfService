# Generated by Django 3.0.5 on 2020-04-26 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_auto_20200426_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='card_info',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='orders',
        ),
    ]