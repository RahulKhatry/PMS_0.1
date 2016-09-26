# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeerecords',
            name='upload',
            field=models.FileField(default=datetime.datetime(2016, 9, 24, 15, 13, 30, 949000, tzinfo=utc), upload_to=b'photos/'),
            preserve_default=False,
        ),
    ]
