# Generated by Django 4.0.6 on 2022-09-09 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Interview', '0004_comment_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
    ]
