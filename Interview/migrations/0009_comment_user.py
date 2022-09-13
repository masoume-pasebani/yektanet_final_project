# Generated by Django 4.0.6 on 2022-09-12 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_applicant_uer_type_and_more'),
        ('Interview', '0008_remove_comment_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.interviewer'),
        ),
    ]