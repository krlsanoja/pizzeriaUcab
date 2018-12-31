from django.db import models

# Create your models here.

class pizza(models.Model):
   size=models.CharField(max_length=200)
   precio=models.FloatField()
   descripcion=models.TextField(max_length=350)


class ingrediente(models.Model):
    nombre=models.CharField(max_length=250)
    precio=models.FloatField()
    descripcion=models.TextField(max_length=350)


class cliente(models.Model):
    ci=models.IntegerField()
    nombre=models.CharField(max_length=250)
    apellido=models.CharField(max_length=250)
    telefono=models.IntegerField()
   

class orden(models.Model):
    fecha=models.DateTimeField('fecha de orden')
    cantidad=models.IntegerField()
    total=models.FloatField()
    fk_pizza=models.ForeignKey(pizza,on_delete=models.CASCADE)
    fk_ingrediente=models.ForeignKey(ingrediente,null=True,blank=True,default=None,on_delete=models.CASCADE)
    fk_cliente=models.ForeignKey(cliente,on_delete=models.CASCADE)

class metodo_pago(models.Model):
  num_pago= models.primary_key=True
 
 
class efectivo(metodo_pago):

  moneda=models.CharField(max_length=60)


class tarjeta(metodo_pago):
    num_tarjeta=models.CharField(max_length=60)
    tipo=models.CharField(max_length=60)


class factura(models.Model):
    fecha_pago=models.DateTimeField('fecha del pago realizado')
    monto_total=models.FloatField()
    fk_orden=models.ForeignKey(orden,on_delete=models.PROTECT)
    fk_metodo=models.ForeignKey(metodo_pago,on_delete=models.PROTECT)