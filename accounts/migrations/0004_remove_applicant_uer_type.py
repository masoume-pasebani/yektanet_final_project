# Generated by Django 4.0.6 on 2022-09-07 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_interviewer_uer_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='uer_type',
        ),
    ]
