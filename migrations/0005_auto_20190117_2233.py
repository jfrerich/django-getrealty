# Generated by Django 2.1 on 2019-01-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realty', '0004_auto_20190117_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='Files_xx_DataF',
            field=models.TextField(default='', verbose_name='Files_xx_DataF'),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='Files_xx_DetF',
            field=models.TextField(default='', verbose_name='Files_xx_DetF'),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='Files_xx_HistF',
            field=models.TextField(default='', verbose_name='Files_xx_HistF'),
        ),
        migrations.AlterField(
            model_name='testmodel',
            name='Property_Interest',
            field=models.TextField(default='', verbose_name='Property_Interest'),
        ),
    ]
