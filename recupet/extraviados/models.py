from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class PerditusPet(models.Model):
    NombreDueñoMascota = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    NombreMascotaExtraviada = models.CharField(max_length=30)
    RazaMascotaExtraviada = models.CharField(max_length=15)
    TipoMascotaExtraviada = models.CharField(max_length=15)
    CaracteristicasMascota = models.CharField(max_length=200)
    Donde = models.CharField(max_length=200)
    cuando = models.DateTimeField()
    contacto = models.IntegerField(max_length = 10)

    
    def Publicar (self):
        self.save()
        
    def __str__(self):
        report = (f'Se Extravió {self.TipoMascotaExtraviada} de raza {self.RazaMascotaExtraviada} con {self.CaracteristicasMascota} en {self.Donde} el dia {self.cuando}, si la vez contactar a {self.NombreDueñoMascota} al número {self.contacto} ')
        return report