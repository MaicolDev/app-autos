from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    año = models.CharField(max_length=4)
    propietario= models.ForeignKey(User,on_delete=models.CASCADE)
    fecha= models.DateTimeField(auto_now_add=True)
    precio= models.FloatField()
    vendido= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.marca} {self.modelo} -de {self.propietario.username}"