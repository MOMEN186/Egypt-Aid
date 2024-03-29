# Generated by Django 5.0.2 on 2024-03-07 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorest', '0008_rename_popualation_village_population'),
    ]

    operations = [
        migrations.CreateModel(
            name='public_safety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
                ('radius', models.IntegerField(default=0)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poorest.center')),
                ('government', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poorest.government')),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poorest.village')),
            ],
        ),
    ]
