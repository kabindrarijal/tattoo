# Generated by Django 2.2.2 on 2019-07-31 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userTime', '0010_remove_usertime_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertime',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usertime',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
