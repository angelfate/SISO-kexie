# Generated by Django 2.0.6 on 2018-08-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadres', '0003_auto_20180822_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadres',
            name='student',
        ),
        migrations.AlterField(
            model_name='cadres',
            name='name',
            field=models.CharField(max_length=20, verbose_name='姓名'),
        ),
    ]