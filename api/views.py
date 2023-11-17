from django.http import JsonResponse

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

    def list(self, request, *args, **kwargs):

        pestanas = Pestanas.objects.prefetch_related('clvtip')

        data = []

        for pestana in pestanas:
            data.append({
                "id": pestana.id,
                "nombre": pestana.nombre,
                "descripcion": pestana.descripcion,
                "foto": pestana.foto,
                "preciopes": pestana.preciopes,
                "hab": pestana.hab,
                "tamano": pestana.tamano,
                "clvtip": pestana.clvtip.id,
                "tipo": pestana.clvtip.nombre
            })

        return JsonResponse({'data': data}, status=status.HTTP_207_MULTI_STATUS)

class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer

    def list(self, request, *args, **kwargs):
        id_cliente = self.request.query_params.get('id_cliente')
        id_tarjeta = self.request.query_params.get('id_tarjeta')

        if not id_cliente and id_tarjeta:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if id_cliente and not id_tarjeta:
            tarjetas = Tarjeta.objects.filter(clvusu_id=id_cliente)
            serialize_data = TarjetaSerializer(tarjetas, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serialize_data.data
            )

        if id_cliente and id_tarjeta:
            tarjeta = Tarjeta.objects.filter(clvusu_id=id_cliente, id=id_tarjeta).first()
            serialize_data = TarjetaSerializer(tarjeta)

            return Response(
                status=status.HTTP_200_OK,
                data=serialize_data.data
            )


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    def list(self, request, *args, **kwargs):
        id_servicio = self.request.query_params.get('id_servicio')

        if id_servicio:
            empleados = Empleado.objects.filter(servicoempleado__clvser=id_servicio)
            ser_empleados = EmpleadoSerializer(empleados, many=True).data
            return Response(status=status.HTTP_200_OK, data=ser_empleados)

        empleados = Empleado.objects.all()
        ser_empleados = EmpleadoSerializer(empleados, many=True).data
        return Response(status=status.HTTP_200_OK, data=ser_empleados)

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ServicioEmpleadoViewSet(viewsets.ModelViewSet):
    queryset = ServicoEmpleado.objects.all()
    serializer_class = ServicioEmpleadoSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

    def list(self, request, *args, **kwargs):
        id_cliente = self.request.query_params.get('id_cliente')

        if id_cliente:
            data = Cita.objects.select_related("clvstat", "clvser").filter(clvusu_id=id_cliente)

            response = []

            for d in data:
                response.append({
                        "id": d.id,
                        "fecha": d.fecha,
                        "hora": d.hora,
                        "precio_final": d.precio_final,
                        "hab": d.hab,
                        "clvusu": d.clvusu.id,
                        "clvser": d.clvser.id,
                        "clvpes": d.clvpes.id,
                        "clvfp": d.clvfp.id,
                        "clvstat": d.clvstat.id,
                        "estatus": d.clvstat.nombre,
                        "servicio": d.clvser.nombre,
                        "foto": "https://www.plasticoncomposites.com/img/team-placeholder.png",
                        "empleado": "Guest"
                    })

            return JsonResponse({"data": response}, status=status.HTTP_200_OK)

        data = CitaSerializer(Cita.objects.all(), many=True).data
        return Response(status=status.HTTP_200_OK, data=data)


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

        user = Usuario.objects.filter(correo_electronico=email, contrasena=password, hab=True).first()
        serialize_data = UsuarioSerializer(user)

        if not user:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"message": "El correo y/o la contraseña son incorrectos", "data": None}
            )

        return Response(
            status=status.HTTP_200_OK,
            data={
                "message": "Sesión iniciada",
                "data": serialize_data.data
            }
        )

    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer
