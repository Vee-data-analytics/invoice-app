# Generated by Django 4.0.1 on 2022-04-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='account_number',
            field=models.CharField(max_length=13),
        ),
    ]
