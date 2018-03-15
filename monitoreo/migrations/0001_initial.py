# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='dispositivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Zona', models.CharField(max_length=150, verbose_name=b'Zona Bogot\xc3\xa1')),
                ('Responsable', models.CharField(max_length=150)),
                ('coordX', models.FloatField(verbose_name=b'Coordenada X')),
                ('coordY', models.FloatField(verbose_name=b'Coordenada X')),
            ],
            options={
                'verbose_name': 'Dispositivo',
                'verbose_name_plural': 'Dispositivos',
            },
        ),
        migrations.CreateModel(
            name='medicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('captura', models.FloatField(verbose_name=b'medicion sensor')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'sensor',
                'verbose_name_plural': 'sensores',
            },
        ),
        migrations.CreateModel(
            name='sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.BooleanField(default=True, verbose_name=b'encendio o apagado')),
                ('variable', models.CharField(max_length=150, choices=[(b'CO', b'CO'), (b'CO2', b'CO2'), (b'RUIDO', b'RUIDO'), (b'TEMPERATURA', b'TEMPERATURA')])),
                ('unidades', models.CharField(max_length=50, choices=[(b'ppm', b'ppm'), (b'ppm', b'ppm'), (b'decibeles', b'decibeles'), (b'\xc2\xb0C', b'\xc2\xb0C')])),
                ('medicion', models.ManyToManyField(to='monitoreo.medicion', null=True, verbose_name=b'mediciones', blank=True)),
            ],
            options={
                'verbose_name': 'sensor',
                'verbose_name_plural': 'sensores',
            },
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='Sensores',
            field=models.ManyToManyField(to='monitoreo.sensor', null=True, verbose_name=b'lista de sensores', blank=True),
        ),
        migrations.AddField(
            model_name='dispositivo',
            name='usuario',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
