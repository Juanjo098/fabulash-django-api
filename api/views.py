from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class FormaPagoViewSet(viewsets.ModelViewSet):
    queryset = FormaPago.objects.all()
    serializer_class = FormaPagoSerializer

class EstatusViewSet(viewsets.ModelViewSet):
    queryset = Estatus.objects.all()
    serializer_class = EstatusSerializer

class PuestoViewSet(viewsets.ModelViewSet):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = TipoSerializer

class PestanasViewSet(viewsets.ModelViewSet):
    queryset = Pestanas.objects.all()
    serializer_class = PestanasSerializer

class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = ServicoEmpleado.objects.all()
    serializer_class = ServicioEmpleadoSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer


















