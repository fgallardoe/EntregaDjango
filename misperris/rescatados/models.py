from django.db import models

# Create your models here.

class Estado(models.Model):
    desc_estado = models.CharField(max_length=20)

    def __str__(self):
        return self.desc_estado


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nom_mascota = models.CharField(max_length=20)
    tamano_mascota = models.IntegerField(default=0)
    peso_mascota = models.FloatField(default=0)
    color_mascota = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=300)
    fecha_rescate = models.DateField('Fecha Rescate')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

#utilizamos una fomra distinta de mostrar los resultados a través de una lista en el admin.
