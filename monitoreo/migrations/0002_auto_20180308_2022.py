# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicion',
            options={'verbose_name': 'medicion', 'verbose_name_plural': 'mediciones'},
        ),
        migrations.AlterField(
            model_name='sensor',
            name='unidades',
            field=models.CharField(max_length=50, choices=[(b'ppm', b'ppm'), (b'deciveles', b'deciveles'), (b'Grados Centigrados', b'Grados Centigrados')]),
        ),
    ]
