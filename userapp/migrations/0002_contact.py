# Generated by Django 5.1.4 on 2024-12-18 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=25)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
