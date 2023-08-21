from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Usuarios(models.Model):
    
    DNI = "DNI"
    CARNET = "CARNET EXT."
    PASAPORTE = "PASAPORTE"
    TipoDocumento = [
        (DNI, "Documento de Identidad"),
        (CARNET, "Carnet de Extranjería"),
        (PASAPORTE, "Pasaporte"),
    ]
    
    GESTOR = "GESTOR"
    SUPERVISOR = "SUPERVISOR"
    ANALISTA = "ANALISTA"
    CONTROLLER = "CONTROLLER"
    TipoUsuario = [
        (GESTOR, "Gestor"),
        (SUPERVISOR, "Supervisor"),
        (ANALISTA, "Analista"),
        (CONTROLLER, "Controller"),
    ]

    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=150)
    primerApellido = models.CharField(max_length=150, db_column='apellido_paterno')
    segundoApellido = models.CharField(max_length=150, db_column='apellido_materno')
    tipoDocumento = models.CharField(choices=TipoDocumento, db_column='tipo_documento')
    numeroDocumento = models.IntegerField(unique=True)
    tipoUsuario = models.CharField(choices=TipoUsuario, db_column='tipo_usuario')
    correo = models.EmailField(max_length=254, unique=True)
    celular = PhoneNumberField(null=False, blank=False)
    fechaCreacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    fechaModifacion = models.DateTimeField(auto_now=True, db_column='fecha_modificacion')
    estaActivo = models.BooleanField(default=True, db_column="esta_activo")

    class Meta:
        db_table = 'usuarios'