# Generated by Django 2.2.2 on 2019-07-31 04:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userTime', '0003_auto_20190731_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertime',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usertime',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 7, 31, 10, 37, 40, 421351)),
        ),
        migrations.AlterField(
            model_name='usertime',
            name='time',
            field=models.TimeField(blank=True, default=datetime.datetime(2019, 7, 31, 4, 52, 40, 421351, tzinfo=utc)),
        ),
    ]
