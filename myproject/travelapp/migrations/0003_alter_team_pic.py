# Generated by Django 4.1.2 on 2022-11-09 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='pic',
            field=models.ImageField(upload_to='picture'),
        ),
    ]
