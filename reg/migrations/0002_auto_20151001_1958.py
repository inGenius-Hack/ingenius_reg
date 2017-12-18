# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='location',
        ),
        migrations.AddField(
            model_name='team',
            name='team_id',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
