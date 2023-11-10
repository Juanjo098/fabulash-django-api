from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=64, null=False)
    apellido = models.CharField(max_length=64, null=False)
    correo_electronico = models.CharField(max_length=64, null=False, unique=True)
    telefono = models.CharField(max_length=10, null=False, unique=True)
    contrasena = models.CharField(max_length=16, null=False)
    hab = models.BooleanField(null=False, default=True)
    def _str_(self):
        return f"{self.nombre} {self.apellido} {self.correo_electronico}"

class FormaPago(models.Model):
    nombre = models.CharField(max_length=32, null=False, unique=True)
    descripcion = models.CharField(max_length=64, null=False)
    hab = models.BooleanField(null=False, default=True)

    def _str_(self):
        return f"{self.nombre} {self.descripcion}"

class Estatus(models.Model):
    nombre = models.CharField(max_length=16, null=False, unique=True)
    hab = models.BooleanField(null=False, default=True)

    def _str_(self):
        return f"{self.nombre}"

class Puesto(models.Model):
    nombre = models.CharField(max_length=64, null=False, unique=True)
    hab = models.BooleanField(null=False, default=True)

    def _str_(self):
        return f"{self.nombre}"

class Tipo(models.Model):
    nombre = models.CharField(max_length=64, null=False, unique=True)
    hab = models.BooleanField(null=False, default=True)

    def _str_(self):
        return f"{self.nombre}"

class Pestanas(models.Model):
    nombre = models.CharField(max_length=32, null=False, unique=True)
    descripcion = models.CharField(max_length=64, null=False)
    foto = models.CharField(max_length=256, default="https://images.squarespace-cdn.com/content/v1/5b9d43fb55b02cec87e4c0ad/1539988476944-U5ZT074DKC5AYSYGXHSY/Screen+Shot+2018-10-19+at+5.32.01+PM.png")
    preciopes = models.FloatField(null=False, default=0)
    hab = models.BooleanField(null=False, default=True)
    clvtip = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.nombre} {self.descripcion}"

class Tarjeta(models.Model):
    nombre = models.CharField(max_length=64, null=False)
    apellido = models.CharField(max_length=64, null=False)
    numero = models.CharField(max_length=16, null=False, unique=True)
    fecha_vencimiento = models.DateField(null=False)
    cvd = models.IntegerField(null=False)
    hab = models.BooleanField(null=False, default=True)
    clvusu = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.nombre} {self.apellido} {self.numero}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=64, null=False)
    apellido = models.CharField(max_length=64, null=False)
    telefono = models.CharField(max_length=10, null=False, unique=True)
    direccion = models.CharField(max_length=64, null=False)
    descripcion = models.CharField(max_length=64, null=False)
    imagen = models.CharField(max_length=256, null=False)
    estrellas = models.IntegerField(null=False, default=0)
    hab = models.BooleanField(null=False, default=True)
    clvpst = models.ForeignKey(Puesto, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.nombre} {self.apellido}"

class Servicio(models.Model):
    nombre = models.CharField(max_length=32, null=False, unique=True)
    descripcion = models.CharField(max_length=64)
    precioser = models.FloatField(null=False, default=0)
    hab = models.BooleanField(null=False, default=True)
    clvemp = models.ManyToManyField(Empleado, through='ServicoEmpleado')

    def _str_(self):
        return f"{self.nombre} {self.descripcion}"

class ServicoEmpleado(models.Model):
    clvser = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=False)
    clvemp = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=False)

    def _str_(self):
        return f"{self.clvser, self.clvemp}"

class Cita(models.Model):
    fecha = models.DateField(null=False)
    hora = models.TimeField(null=False)
    precio_final = models.FloatField(null=False, default=0)
    hab = models.BooleanField(null=False, default=True)
    clvusu = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    clvser = models.ForeignKey(Servicio, on_delete=models.CASCADE, null=False)
    clvpes = models.ForeignKey(Pestanas, on_delete=models.CASCADE, null=True)
    clvfp = models.ForeignKey(FormaPago, on_delete=models.CASCADE, null=False)
    clvstat = models.ForeignKey(Estatus, on_delete=models.CASCADE, null=False)

    def _str_(self):
        return f"{self.fecha} {self.hora} {self.precio_final}"