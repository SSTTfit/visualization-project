# Generated by Django 2.1.7 on 2019-03-27 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myechartsite', '0006_disegenderage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userindicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('ph', models.FloatField()),
                ('ph_c', models.CharField(max_length=128)),
                ('nbz', models.FloatField()),
                ('nbz_c', models.CharField(max_length=128)),
                ('ndy', models.FloatField()),
                ('ndy_c', models.CharField(max_length=128)),
                ('wldb', models.FloatField()),
                ('wldb_c', models.CharField(max_length=128)),
                ('khxs', models.FloatField()),
                ('khxs_c', models.CharField(max_length=128)),
                ('jg', models.FloatField()),
                ('jg_c', models.CharField(max_length=128)),
                ('dbz', models.FloatField()),
                ('dbz_c', models.CharField(max_length=128)),
                ('g', models.FloatField()),
                ('g_c', models.CharField(max_length=128)),
                ('yxsy', models.FloatField()),
                ('yxsy_c', models.CharField(max_length=128)),
                ('qx', models.FloatField()),
                ('qx_c', models.CharField(max_length=128)),
                ('bxb', models.FloatField()),
                ('bxb_c', models.CharField(max_length=128)),
                ('dhs', models.FloatField()),
                ('dhs_c', models.CharField(max_length=128)),
                ('ptt', models.FloatField()),
                ('ptt_c', models.CharField(max_length=128)),
                ('tt', models.FloatField()),
                ('tt_c', models.CharField(max_length=128)),
            ],
        ),
    ]