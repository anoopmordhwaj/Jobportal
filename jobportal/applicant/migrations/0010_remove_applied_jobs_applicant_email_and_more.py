# Generated by Django 4.2.5 on 2023-10-11 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0009_alter_applied_jobs_applicant_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applied_jobs',
            name='applicant_email',
        ),
        migrations.RemoveField(
            model_name='applied_jobs',
            name='applicant_name',
        ),
    ]
