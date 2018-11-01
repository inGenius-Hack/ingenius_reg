# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0003_auto_20181101_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='domain',
            field=models.CharField(max_length=10, blank=True, choices=[('hardware', 'Hardware'), ('iot', 'Internet of Things'), ('ml', 'Machine Learning'), ('mobile', 'Mobile'), ('web', 'Web'), ('zwibe', 'Zwibe')]),
        ),
        migrations.AlterField(
            model_name='team',
            name='idea',
            field=models.TextField(blank=True),
        ),
    ]
