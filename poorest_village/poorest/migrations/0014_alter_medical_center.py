# Generated by Django 5.0.2 on 2024-03-10 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorest', '0013_alter_infrastructure_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medical',
            name='center',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poorest.center'),
        ),
    ]
