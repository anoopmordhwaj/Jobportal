# Generated by Django 4.2.5 on 2023-10-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0002_delete_employer_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applied_jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_resume', models.FileField(upload_to='')),
                ('applicant_coverletter', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='applicant_address',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='applicant_education',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='applicant_skills',
            field=models.CharField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='disability_type',
            field=models.CharField(max_length=5000),
        ),
    ]
