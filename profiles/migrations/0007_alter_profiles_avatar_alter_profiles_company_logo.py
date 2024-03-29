# Generated by Django 4.0.1 on 2022-05-05 13:25

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_profiles_bank_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(upload_to='profilepics'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='company_logo',
            field=imagekit.models.fields.ProcessedImageField(upload_to='company_logo'),
        ),
    ]
