from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre= models.CharField(max_length=128)
    def __str__(self):
        return self.nombre

class expedientes(models.Model):
    nro_expediente = models.IntegerField()
    nro_pago = models.IntegerField()
    detalles = models.CharField()
    año = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=3)
    provedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    

  



