# Generated by Django 2.1 on 2019-01-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_num', models.TextField(default='', max_length=100, verbose_name='r_num')),
            ],
            options={
                'db_table': 'RNUMBERS_Bastrop',
            },
        ),
    ]