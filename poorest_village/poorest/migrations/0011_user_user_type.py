# Generated by Django 5.0.2 on 2024-03-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorest', '0010_rename_specilization_medical_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('viewer', 'viewer'), ('admin', 'admin')], default='viewer', max_length=10),
        ),
    ]
