from django.contrib import admin
from monitoreo.models import dispositivo, sensor, medicion

# Register your models here.
admin.site.index_title = "Monitoreo"
admin.site.register(dispositivo)
admin.site.register(sensor)
admin.site.register(medicion)