# Generated by Django 3.0.5 on 2020-04-28 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ready_Hands_API', '0012_auto_20200427_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='hour_rate',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
