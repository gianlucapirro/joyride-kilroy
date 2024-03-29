# Generated by Django 4.1.7 on 2023-06-08 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, default='', max_length=255)),
                ('roadtrip', models.CharField(max_length=1000)),
                ('email_friend1', models.EmailField(max_length=254)),
                ('email_friend2', models.EmailField(max_length=254)),
            ],
        ),
    ]
