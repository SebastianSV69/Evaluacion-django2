from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    numero = models.CharField(max_length=16)
    fecharegistro = models.DateTimeField()

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Atencion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    horarioAtencion = models.DateField()
    precio = models.PositiveIntegerField()
    Cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='Atencion',
    )

    def __str__(self):
        return self.nombre
