# Generated by Django 4.1.2 on 2022-11-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nams', models.CharField(max_length=250)),
                ('pic', models.ImageField(upload_to='pics')),
                ('descr', models.TextField()),
            ],
        ),
    ]
