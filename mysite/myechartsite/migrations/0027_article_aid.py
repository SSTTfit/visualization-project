# Generated by Django 2.1.7 on 2019-05-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myechartsite', '0026_auto_20190429_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='aid',
            field=models.IntegerField(default=201905081),
        ),
    ]
