# Generated by Django 3.2.4 on 2021-06-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_destination_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='auther',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]