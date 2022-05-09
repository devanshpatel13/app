# Generated by Django 4.0.4 on 2022-05-09 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]