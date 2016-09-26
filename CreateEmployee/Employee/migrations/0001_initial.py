# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeRecords',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('EName', models.CharField(max_length=60)),
                ('HiringDate', models.DateField(help_text=b'date published')),
                ('emailID', models.CharField(max_length=60)),
            ],
        ),
    ]
