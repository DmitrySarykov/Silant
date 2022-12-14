# Generated by Django 4.1.3 on 2022-11-07 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_alter_maintenance_service_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='downtime',
            field=models.PositiveIntegerField(default=0, verbose_name='Время простоя техники'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='service_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.servicecompany', verbose_name='Сервисная компания'),
        ),
    ]
