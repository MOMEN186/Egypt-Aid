# Generated by Django 5.0.2 on 2024-03-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorest', '0004_rename_governnment_holly_places_government_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='holly_places',
            name='availability',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='infrastructure',
            name='availability',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medical',
            name='availability',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='school',
            name='availability',
            field=models.BooleanField(default=False),
        ),
    ]
