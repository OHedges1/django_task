# Generated by Django 4.0.1 on 2022-01-20 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryCodes',
            fields=[
                ('country_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('local_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='holidays.countrycodes')),
            ],
        ),
    ]
