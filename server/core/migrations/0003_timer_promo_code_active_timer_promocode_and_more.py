# Generated by Django 4.0.5 on 2022-10-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_timer'),
    ]

    operations = [
        migrations.AddField(
            model_name='timer',
            name='promo_code_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='timer',
            name='promocode',
            field=models.CharField(default='NTH22', max_length=100),
        ),
        migrations.AlterField(
            model_name='timer',
            name='time',
            field=models.IntegerField(default=1666971000000),
        ),
    ]
