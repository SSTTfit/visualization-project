# Generated by Django 2.1.7 on 2019-06-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myechartsite', '0028_auto_20190508_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='userindicator',
            name='name',
            field=models.CharField(default='test', max_length=128),
        ),
    ]
