# Generated by Django 2.1.7 on 2019-04-24 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myechartsite', '0022_auto_20190424_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='collector',
            field=models.ManyToManyField(to='myechartsite.User'),
        ),
    ]