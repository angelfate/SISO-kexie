# Generated by Django 2.0.6 on 2018-08-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='name',
            field=models.CharField(max_length=100, verbose_name='我们的历史'),
        ),
        migrations.AlterField(
            model_name='whos',
            name='name',
            field=models.CharField(max_length=100, verbose_name='我们是谁'),
        ),
    ]