# Generated by Django 3.0.4 on 2020-03-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='f_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='telnum',
            name='tel_num',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
