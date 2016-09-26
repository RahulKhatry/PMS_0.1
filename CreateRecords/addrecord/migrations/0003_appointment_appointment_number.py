# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addrecord', '0002_auto_20160925_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Appointment_Number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
