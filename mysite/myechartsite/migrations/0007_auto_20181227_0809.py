# Generated by Django 2.1.4 on 2018-12-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myechartsite', '0006_user_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.CharField(default='custome', max_length=128),
        ),
    ]