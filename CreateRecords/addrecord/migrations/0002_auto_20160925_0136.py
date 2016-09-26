# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addrecord', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='Appointment',
            new_name='Appointment_Date',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Appointment_Time',
            field=models.TimeField(help_text=b'hh:mm:ss'),
        ),
    ]
