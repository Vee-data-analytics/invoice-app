# Generated by Django 4.0.1 on 2022-04-19 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_client_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_address',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='logo',
            field=models.ImageField(blank=True, default='images/no_photo.png', upload_to=''),
        ),
    ]
