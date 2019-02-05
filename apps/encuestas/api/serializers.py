from rest_framework import serializers
from ..models import Encuesta, Pregunta, OpcionPregunta, Resultado
from django.contrib.auth.models import User



class ResultadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resultado
        fields = '__all__'


class OpcionPreguntaSerializer(serializers.ModelSerializer):
    resultados = ResultadoSerializer(many=True, required=False)

    class Meta:
        model = OpcionPregunta
        fields = '__all__'


class PreguntaSerializer(serializers.ModelSerializer):
    opciones = OpcionPreguntaSerializer(many=True, required=False)

    class Meta:
        model = Pregunta
        fields = '__all__'


class EncuestaSerializer(serializers.ModelSerializer):
    preguntas = PreguntaSerializer(many=True, required=False)

    class Meta:
        model = Encuesta
        fields = '__all__'




