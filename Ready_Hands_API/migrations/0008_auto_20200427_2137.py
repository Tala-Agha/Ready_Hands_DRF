# Generated by Django 3.0.5 on 2020-04-27 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ready_Hands_API', '0007_auto_20200427_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
