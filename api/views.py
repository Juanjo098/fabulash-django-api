
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response


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
    queryset = Tipo.objects.all()
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

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = LoginSerializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request, *args, **kwargs):
        email = request.data.get('correo_electronico')
        password = request.data.get('contrasena')

        if not email or not password:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": "Llena los campos"}
            )

        user = Usuario.objects.filter(correo_electronico=email, contrasena=password).first()

        if not user:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data={"message": "El correo y/o la contraseña son incorrectos"}
            )

        return Response(
            status=status.HTTP_200_OK,
            data={
                "message": "Sesión iniciada",
                "data": {
                    "user_id": user.id,
                    "username": f"{user.nombre} {user.apellido}"
                }
            }
        )

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
