# Generated by Django 2.1.7 on 2019-03-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myechartsite', '0004_diseage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseage',
            name='year',
            field=models.IntegerField(),
        ),
    ]
