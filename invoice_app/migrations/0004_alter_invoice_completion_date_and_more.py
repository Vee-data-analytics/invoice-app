# Generated by Django 4.0.1 on 2022-04-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0003_alter_invoice_completion_date_alter_invoice_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='completion_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='issued_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payement_date',
            field=models.DateField(),
        ),
    ]