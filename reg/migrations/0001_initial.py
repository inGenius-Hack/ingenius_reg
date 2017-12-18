# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('participant_id', models.CharField(unique=True, max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('college', models.CharField(max_length=100)),
                ('github_url', models.URLField(null=True, blank=True)),
                ('linkedin_url', models.URLField(null=True, blank=True)),
                ('barcode', models.CharField(max_length=50, blank=True)),
                ('recharge_possible', models.BooleanField(default=True)),
                ('service_provider', models.CharField(max_length=50, blank=True)),
                ('registered', models.BooleanField(default=False)),
                ('checked_in', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('noc_submitted', models.NullBooleanField()),
                ('had_lunch', models.BooleanField(default=False)),
                ('had_dinner', models.BooleanField(default=False)),
                ('had_breakfast', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('idea', models.TextField()),
                ('domain', models.CharField(blank=True, max_length=10, choices=[(b'hardware', b'Hardware'), (b'iot', b'Internet of Things'), (b'ml', b'Machine Learning'), (b'mobile', b'Mobile'), (b'web', b'Web'), (b'zwibe', b'Zwibe')])),
                ('location', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='team',
            field=models.ForeignKey(related_name='participants', to='reg.Team'),
        ),
    ]
