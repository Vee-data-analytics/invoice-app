# Generated by Django 4.0.1 on 2022-04-20 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('positions', '0002_position_price_position_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='amount',
            field=models.FloatField(help_text='in Rands'),
        ),
    ]
