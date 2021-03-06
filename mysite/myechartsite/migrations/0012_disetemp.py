# Generated by Django 2.1.7 on 2019-04-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myechartsite', '0011_auto_20190411_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disetemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('year', models.IntegerField()),
                ('temp20_15', models.FloatField()),
                ('temp15_10', models.FloatField()),
                ('temp10_5', models.FloatField()),
                ('temp5_0', models.FloatField()),
                ('temp0_5', models.FloatField()),
                ('temp5_10', models.FloatField()),
                ('temp10_15', models.FloatField()),
                ('temp15_20', models.FloatField()),
                ('temp20_25', models.FloatField()),
                ('temp25_30', models.FloatField()),
                ('temp30_35', models.FloatField()),
                ('temp35_40', models.FloatField()),
            ],
        ),
    ]
