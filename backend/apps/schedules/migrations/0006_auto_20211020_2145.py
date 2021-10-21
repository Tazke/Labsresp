# Generated by Django 3.2 on 2021-10-20 21:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0005_auto_20211020_1904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petition',
            old_name='campus',
            new_name='campus_petition',
        ),
        migrations.AddField(
            model_name='schedule',
            name='day',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 20, 21, 43, 16, 338616), null=True),
        ),
        migrations.AlterField(
            model_name='petition',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 20, 21, 43, 16, 337791), null=True),
        ),
    ]
