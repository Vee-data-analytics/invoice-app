# Generated by Django 4.0.1 on 2022-04-19 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estimates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, help_text='optional')),
                ('amount', models.FloatField(help_text='in Rands')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('estimate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estimates.estimate')),
            ],
        ),
    ]