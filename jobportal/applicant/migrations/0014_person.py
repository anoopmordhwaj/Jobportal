# Generated by Django 4.2.5 on 2024-03-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0013_alter_applied_jobs_applicant_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
