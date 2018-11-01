# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0007_auto_20181101_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='noc_submitted',
            field=models.BooleanField(default=True),
        ),
    ]
