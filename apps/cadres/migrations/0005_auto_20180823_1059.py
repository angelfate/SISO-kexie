# Generated by Django 2.0.6 on 2018-08-23 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadres', '0004_auto_20180822_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadres',
            name='image',
            field=models.ImageField(default='image/default.jpg', upload_to='cardes/%Y%m', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='cadres',
            name='name',
            field=models.CharField(max_length=20, verbose_name='名字'),
        ),
    ]
