# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50)),
                ('Appointment', models.DateField(help_text=b'dd/mm/yy')),
                ('Appointment_Time', models.TimeField(help_text=b'hh/mm/ss')),
                ('Phone', models.IntegerField()),
                ('emailID', models.CharField(max_length=60)),
            ],
        ),
    ]
