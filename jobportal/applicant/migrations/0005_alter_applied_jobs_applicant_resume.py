# Generated by Django 4.2.5 on 2023-10-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0004_alter_applied_jobs_applicant_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applied_jobs',
            name='applicant_resume',
            field=models.FileField(null=True, upload_to='resume'),
        ),
    ]
