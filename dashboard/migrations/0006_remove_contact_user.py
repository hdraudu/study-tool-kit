# Generated by Django 4.0 on 2022-08-30 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]
