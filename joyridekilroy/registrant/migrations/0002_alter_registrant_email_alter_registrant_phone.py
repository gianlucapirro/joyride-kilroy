# Generated by Django 4.1.7 on 2023-06-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrant',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='registrant',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=255, unique=True),
        ),
    ]
