# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_auto_20151001_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='gender',
            field=models.CharField(max_length=1),
        ),
    ]
