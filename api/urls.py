from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'formapago', views.FormaPagoViewSet)
router.register(r'estatus', views.EstatusViewSet)
router.register(r'puesto', views.PuestoViewSet)
router.register(r'tipo', views.TipoViewSet)
router.register(r'pestanas', views.PestanasViewSet)
router.register(r'tarjeta', views.TarjetaViewSet)
router.register(r'empleado', views.EmpleadoViewSet)
router.register(r'servicio', views.ServicioViewSet)
router.register(r'servicioempleado', views.ServicioEmpleadoViewSet)
router.register(r'cita', views.CitaViewSet)
router.register(r'login', views.LoginViewSet)
router.register(r'resenas', views.ResenaViewSet)
router.register(r'proxima-cita', views.ProximaListApiView)

urlpatterns = [
    path('', include(router.urls)),
]