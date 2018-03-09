from django.shortcuts import render
from . import models
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
from monitoreo.models import dispositivo
from django.core.urlresolvers import reverse_lazy
from django.template import loader
# Create your views here.
class DispositivoIndex(ListView):
    queryset = models.dispositivo.objects.all()
    template_name = "home.html"
    paginate_by = 9


class DispositivoDetail(DetailView):
    model = models.dispositivo
    template_name = "dispositivodetalle.html"