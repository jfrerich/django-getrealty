# Generated by Django 2.1 on 2019-01-17 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='Property_Interest',
            field=models.TextField(default='', max_length=100, verbose_name='Property_Interest'),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='rpg',
            field=models.TextField(default='', verbose_name='rpg'),
        ),
    ]
