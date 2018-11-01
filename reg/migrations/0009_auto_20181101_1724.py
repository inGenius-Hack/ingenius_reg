# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0008_auto_20181101_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='had_snacks_evening',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='had_snacks_midnight',
            field=models.BooleanField(default=False),
        ),
    ]
