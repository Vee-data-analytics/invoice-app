# Generated by Django 4.0.1 on 2022-04-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profiles_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='company_reg_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profiles',
            name='vat_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
