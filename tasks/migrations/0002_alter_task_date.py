# Generated by Django 4.2.7 on 2023-12-10 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 12, 10, 12, 45, 15, 620037)),
        ),
    ]
