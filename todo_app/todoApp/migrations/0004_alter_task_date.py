# Generated by Django 3.2.9 on 2021-11-04 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0003_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
