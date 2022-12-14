# Generated by Django 4.1.3 on 2022-11-06 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlledbridge',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='drivingbridge',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='engine',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='technic',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='transmission',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
