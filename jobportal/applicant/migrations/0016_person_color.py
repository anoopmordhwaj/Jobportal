# Generated by Django 4.2.5 on 2024-03-11 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0015_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='color', to='applicant.color'),
        ),
    ]
