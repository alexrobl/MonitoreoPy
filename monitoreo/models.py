#-*- coding:utf-8 -*-
from django.db import models
import os
from django.core.urlresolvers import reverse

# opciones de sensor.
SENSOR_CHOICES =(
	('CO', 'CO'),
	('CO2', 'CO2'),
	('RUIDO', 'RUIDO'),
	('TEMPERATURA', 'TEMPERATURA'),
	)
UNIDADES_CHOICES =(
	('ppm', 'ppm'),
	('deciveles', 'deciveles'),
	('Grados Centigrados', 'Grados Centigrados'),
	)
class medicion(models.Model):
	captura = models.FloatField(verbose_name ='medicion sensor')
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%.3f' % (self.captura)

	class Meta:
		verbose_name = "medicion"
		verbose_name_plural = "mediciones"
#creamos el modelo para el sensor
class sensor(models.Model):
	#asignar un campo nombre para cada sensor diferente#
	estado = models.BooleanField(default=True,verbose_name ='encendio o apagado')
	variable = models.CharField(max_length=150, choices = SENSOR_CHOICES )
	unidades = models.CharField(max_length=50, choices = UNIDADES_CHOICES )
	medicion = models.ManyToManyField(medicion, verbose_name ='mediciones',null=True, blank=True)
	

	def __unicode__(self):
		return  os.path.basename(self.variable)

	class Meta:
		verbose_name = "sensor"
		verbose_name_plural = "sensores"

# creamos el modelo de dispositivo
class dispositivo(models.Model):
	slug = models.SlugField(max_length=200, unique=True)
	Zona = models.CharField(max_length=150, verbose_name ='Zona Bogotá')
	Responsable = models.CharField(max_length=150)
	coordX = models.FloatField(verbose_name ='Coordenada X')
	coordY = models.FloatField(verbose_name ='Coordenada X')
	usuario =  models.ForeignKey('auth.User', blank=True, null=True,
                                   default=None)
	Sensores = models.ManyToManyField(sensor, verbose_name ='lista de sensores',null=True, blank=True)


	def __unicode__(self):
		return  os.path.basename(self.Zona)
	def get_absolute_url(self):
		return reverse("entry_detail", kwargs={"slug": self.slug})
	class Meta:
		verbose_name = "Dispositivo"
		verbose_name_plural = "Dispositivos"


