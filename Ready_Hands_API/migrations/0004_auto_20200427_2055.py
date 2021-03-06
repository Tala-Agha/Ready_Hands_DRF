# Generated by Django 3.0.5 on 2020-04-27 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ready_Hands_API', '0003_auto_20200427_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_no',
            field=models.IntegerField(verbose_name='phone_no'),
        ),
    ]
