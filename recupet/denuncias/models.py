from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Complaint(models.Model):
    Reportero = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Abandono = 'AB'
    Maltrato = 'MT'
    Choise= [
        (Abandono, 'Abandono'),
        (Maltrato, 'Maltrato'),
    ]
    TipoDenuncia = models.CharField(max_length=20,choices=Choise,default='Maltrato')
    Descripcion = models.CharField(max_length=255)
    TipoMascotaExtraviada = models.CharField(max_length=15)
    CaracteristicasMascota = models.CharField(max_length=200)
    Donde = models.CharField(max_length=200)
    cuando = models.DateTimeField()

    
    def Publicar (self):
        self.save()
        
    def __str__(self):
        if self.TipoDenuncia=='MT':
            report = (f'En {self.Donde}, hay un caso de MALTRATO, {self.Descripcion}, esto ocurrió {self.cuando}, se solcita acompañamiento de defensores animales ')
        else: 
            report = (f'En {self.Donde}, hay un caso de ABANDONO, {self.Descripcion}, esto ocurrió {self.cuando}, se solicita personas interesadas en adoptar ')

        return report