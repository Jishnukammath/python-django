# Generated by Django 3.2.4 on 2021-06-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('image', models.ImageField(upload_to='pictures')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]