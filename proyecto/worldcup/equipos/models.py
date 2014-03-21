from django.db import models

# Create your models here.
POSICIONES = (
    ('selecione', 'Seleccione'),
    ('arquero', 'Arquero'),
    ('defensa', 'Defensa'),
    ('delantero', 'Delantero'),
    ('volante', 'Volante'),
)


class Continente(models.Model):
    nombreContinente = models.CharField(max_length=50)

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    continente = models.ForeignKey(Continente)
    tecnico = models.CharField(max_length=60)

class Jugador(models.Model):
    nombreJugador = models.CharField(max_length=60)
    posicion = models.CharField(choices=POSICIONES, default= 'seleccione', max_length=10)
    foto = models.ImageField(upload_to='images', verbose_name='Foto', null=True,)
    def __unicode__(self):
        return self.nombreJugador



