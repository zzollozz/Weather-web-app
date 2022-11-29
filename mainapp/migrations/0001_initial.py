# Generated by Django 4.1.2 on 2022-10-31 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50, unique=True, verbose_name='Название города')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ('city_name',),
            },
        ),
        migrations.CreateModel(
            name='DataWeather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(verbose_name='дата')),
                ('temperature', models.IntegerField(verbose_name='Температура')),
                ('weather', models.CharField(max_length=50, verbose_name='Погода')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Погода',
                'verbose_name_plural': 'Погодные условия',
            },
        ),
    ]