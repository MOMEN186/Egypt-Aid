# Generated by Django 5.0.2 on 2024-03-10 19:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorest', '0015_alter_medical_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poorest.village'),
        ),
    ]
