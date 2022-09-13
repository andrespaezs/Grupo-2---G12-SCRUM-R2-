from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class RecoverPet(models.Model):
    NombreQuienEncuentra = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    RazaMascotaEncontrada = models.CharField(max_length=15)
    TipoMascotaEncontrada = models.CharField(max_length=15)
    CaracteristicasMascota = models.CharField(max_length=200)
    Donde = models.CharField(max_length=200)
    cuando = models.DateTimeField()
    contacto = models.IntegerField(max_length = 10)

    
    def Publicar (self):
        self.save()
        
    def __str__(self):
        report = (f'Se encontró {self.TipoMascotaEncontrada} de raza {self.RazaMascotaEncontrada} con {self.CaracteristicasMascota} en {self.Donde} el dia {self.cuando} para mayor información contactar a {self.NombreQuienEncuentra} al número {self.contacto} ')
        return report