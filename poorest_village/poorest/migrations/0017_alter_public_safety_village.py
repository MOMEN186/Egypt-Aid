# Generated by Django 5.0.2 on 2024-03-10 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorest', '0016_alter_medical_village'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public_safety',
            name='village',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='poorest.village'),
        ),
    ]
