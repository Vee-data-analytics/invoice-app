# Generated by Django 4.0.1 on 2022-05-16 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0004_alter_position_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='sub_total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
