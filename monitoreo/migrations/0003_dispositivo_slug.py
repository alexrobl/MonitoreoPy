# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0002_auto_20180308_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='slug',
            field=models.SlugField(default=1, unique=True, max_length=200),
            preserve_default=False,
        ),
    ]
