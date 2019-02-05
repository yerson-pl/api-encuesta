from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid as uuid_lib
# Create your models here.


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "TimeStampModel"
        verbose_name_plural = "TimeStampModels"
        abstract = True


class Encuesta(TimeStampModel):
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Encuesta"
        verbose_name_plural = "Encuestas"

    def __str__(self):
        return self.titulo


class Pregunta(models.Model):
    PREGUNTA_ABIERTA = 'PA'
    PREGUNTA_CERRADA = 'PC'
    PREGUNTA_OPCION_MULTIPLE = 'POM'

    PREGUNTA_CHOICES = (
        (PREGUNTA_ABIERTA, 'Abierta'),
        (PREGUNTA_CERRADA, 'Cerrada'),
        (PREGUNTA_OPCION_MULTIPLE, 'Opcion Multiple')
    )
    encuesta = models.ForeignKey(
        Encuesta,
        related_name='preguntas',
        on_delete=models.CASCADE)
    tipo = models.CharField(max_length=2, choices=PREGUNTA_CHOICES)
    titulo = models.CharField(max_length=300)
    descripcion = models.TextField()
    obligatoria = models.BooleanField()

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

    def __str__(self):
        return self.titulo


class OpcionPregunta(models.Model):
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    opcion = models.CharField(max_length=500)

    class Meta:
        verbose_name = "OpcionPregunta"
        verbose_name_plural = "OpcionPreguntas"

    def __str__(self):
        return self.opcion


class Resultado(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion = models.ForeignKey(OpcionPregunta, related_name='resultados', on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=500)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Resultado"
        verbose_name_plural = "Resultados"

    def __str__(self):
        return self.respuesta