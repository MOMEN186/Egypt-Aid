# Generated by Django 5.0.2 on 2024-03-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poorest', '0011_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='holly_places',
            name='type',
            field=models.CharField(choices=[('mosque', 'mosque'), ('church', 'church')], default='mosque', max_length=10),
        ),
        migrations.AddField(
            model_name='village',
            name='rating',
            field=models.CharField(choices=[('unknown', 'unknown'), ('POOR', 'POOR'), ('GOOD', 'GOOD'), ('VERY GOOD', 'VERY GOOD'), ('EXCELLENT', 'EXCELLENT')], default='unknown', max_length=10),
        ),
        migrations.AlterField(
            model_name='school',
            name='level',
            field=models.CharField(choices=[('unknown', 'unknown'), ('kinderkarten', 'kindergarten'), ('primary', 'primary'), ('secondary', 'secondary'), ('high', 'high')], max_length=20),
        ),
    ]