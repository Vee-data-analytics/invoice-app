# Generated by Django 4.0.1 on 2022-04-12 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_app', '0005_alter_invoice_payement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='issued_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
