# Generated by Django 4.0.1 on 2022-04-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_alter_client_client_address_alter_client_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='company_reg_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='vat_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]