from django.db import models

# Create your models here.
class voto(models.Model):
    VOTO_CHOICES = [
        ('DC', 'DOCE'),
        ('SL', 'SALGADO'),
    ]
    voto = models.CharField(max_length=2,choices=VOTO_CHOICES)

    def __str__(self):
        return self.voto
