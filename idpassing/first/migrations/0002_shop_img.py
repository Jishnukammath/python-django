# Generated by Django 3.2.4 on 2021-10-21 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='images'),
            preserve_default=False,
        ),
    ]
